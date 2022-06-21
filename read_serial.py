#!/usr/bin/env python
import time
import serial
import csv

ser = serial.Serial(
	port = '/dev/ttyS0',
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1,
)


ser.flushInput()
while 1:
    try:
        time.sleep(30)
        data = ser.readline()                                       # Read serial data
        decoded_bytes = data[0:len(data)-2].decode("utf-8")
        with open("data.csv","a") as f:                             # Append serial data into csv file
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.time(), decoded_bytes])
    except:
        print("Exception")
        break