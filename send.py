#!/usr/bin/env python
import serial
import time
import sys

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1.1)

ser.write(sys.argv[1])
