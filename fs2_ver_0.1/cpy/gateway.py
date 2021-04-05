import board
import busio
import digitalio
import adafruit_rfm9x
import struct
import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests
import time

from secrets import secrets

#print(secrets["ssid"])

FULL_URL = secrets["base_url"]+secrets["public_key"]

data_format='fff' 

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# define and set up RFM95 pins and object
RFM95_CS = board.IO33
RFM95_RST = board.IO38

cs = digitalio.DigitalInOut(RFM95_CS)
reset = digitalio.DigitalInOut(RFM95_RST)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)

# Radio loop
while True:
    packet = rfm9x.receive(timeout=5.0)
    if packet is not None:
        print(packet)
        var=struct.unpack(data_format,packet)
        print(var)
        print(var[0])

        wifi.radio.connect(secrets["ssid"], secrets["password"])
        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())
        json_data={"temperature_c":var[1],"humidity_rh":var[2],"private_key":secrets["private_key"],"node_id":var[0]}
        response = requests.post(FULL_URL, json=json_data)
        print(response.text)
        response.close()

        time.sleep(10)


    print('loop')