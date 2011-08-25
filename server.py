#!/usr/bin/env python
# Echo server program
import socket
import serial
import time
import sys

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1.1)

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while(True):
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: conn.close()
    ser.write(data)

