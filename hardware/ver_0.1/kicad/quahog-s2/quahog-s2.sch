EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L esp32-s2:esp32-s2-wroom U1
U 1 1 60673143
P 2950 2900
F 0 "U1" H 2900 4115 50  0000 C CNN
F 1 "esp32-s2-wroom" H 2900 4024 50  0000 C CNN
F 2 "footprints:esp32-s2-wrooom" H 2450 3600 50  0001 C CNN
F 3 "" H 2450 3600 50  0001 C CNN
	1    2950 2900
	1    0    0    -1  
$EndComp
$Comp
L RF_Module:RFM95W-915S2 U2
U 1 1 6067421E
P 6900 2400
F 0 "U2" H 6900 3081 50  0000 C CNN
F 1 "RFM95W-915S2" H 6900 2990 50  0000 C CNN
F 2 "footprints:RFM95" H 3600 4050 50  0001 C CNN
F 3 "https://www.hoperf.com/data/upload/portal/20181127/5bfcbea20e9ef.pdf" H 3600 4050 50  0001 C CNN
	1    6900 2400
	1    0    0    -1  
$EndComp
$Comp
L Connector:USB_C_Receptacle_USB2.0 J?
U 1 1 6067761F
P 2600 5350
F 0 "J?" H 2707 6217 50  0000 C CNN
F 1 "USB_C_Receptacle_USB2.0" H 2707 6126 50  0000 C CNN
F 2 "" H 2750 5350 50  0001 C CNN
F 3 "https://www.usb.org/sites/default/files/documents/usb_type-c.zip" H 2750 5350 50  0001 C CNN
	1    2600 5350
	1    0    0    -1  
$EndComp
$EndSCHEMATC
