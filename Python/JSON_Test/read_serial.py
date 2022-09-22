#!/usr/bin/env python
import time
import serial
import json

# IMPORTANT: sudo RASPI-CONFIG -> ENABLE SERIAL

ser = serial.Serial(
	port = '/dev/ttyS0',
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1,
)

def update_json(topic, field, value):
    with open("data.json", "r") as jsonfile:
        data = json.load(jsonfile)

    if (topic != "general" or topic != "modules" or topic != "phases"):
        data[topic][field] = str(value)

    with open("data.json", "w") as jsonfile:
        json.dump(data, jsonfile)

def read():    
    data = ser.readline()
    decoded_data = data[0:len(data) - 2].decode("utf-8")
    return decoded_data
 
ser.flushInput()

while 1:
    try:
        time.sleep(0.01)
        if(read() == "S"): # If surge data is coming through serial
            update_json("general","surge",str(read()))
        if(read() == "T"): # If tov data is coming through serial
            update_json("general","tov",str(read()))
        if(read() == "C"): # If carrier data is coming through serial
            update_json("general","carrier",str(read()))
        if(read() == "P"): # If power system data is coming through serial
            update_json("general","power_sytem",str(read()))
        
        if(read() == "M"): # If module status data is coming through serial
            topic = "general"
            field = "module_status_"
            for k in range(6):
                update_json(topic, field + (k+1), str(read()))

        if(read() == "L"): # If line presence data is coming through serial
            update_json("phases", "a", str(read()))
            update_json("phases", "b", str(read()))
            update_json("phases", "c", str(read()))

    except:
        print("Exception")
        break