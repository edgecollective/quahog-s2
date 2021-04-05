import board
import busio
import digitalio
import adafruit_rfm9x
import json
import struct

data_format='ff' 

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
        #packet_text = str(packet, 'ascii')
        #print('Received: {0}'.format(packet_text))
        #json_data=json.load(packet_text)
        #print(json_data)
    print('loop')