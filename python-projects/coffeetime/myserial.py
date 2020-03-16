#!/usr/bin/python

## Serial Communication Tools

## Copyright (c) 2015, Augusto Damasceno.
## All rights reserved.
## Redistribution and use in source and binary forms, with or without modification,
## are permitted provided that the following conditions are met:
##   1. Redistributions of source code must retain the above copyright notice,
##      this list of conditions and the following disclaimer.
##   2. Redistributions in binary form must reproduce the above copyright notice,
##      this list of conditions and the following disclaimer in the documentation
##      and/or other materials provided with the distribution.
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
## ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
## WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
## IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
## INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
## BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
## OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
## WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
## ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
## OF SUCH DAMAGE.

import serial
import sys

def serial_discover():
    ser = serial.Serial()
    list = []
    print("\nSearch for available ports:\n")
    if sys.platform == 'win32':
        for i in range(256):
            try:
                ser.port = i
                ser.open()
                list.append(i)
                ser.close()
            except Exception as e:
                print("Error open serial port" + str(e))
    elif sys.platform == 'linux2':
        for i in range(10):
            try:
                if i < 5:
                    ser.port = '/dev/ttyUSB' + str(i)
                    ser.open()
                    list.append('/dev/ttyUSB' + str(i))
                    ser.close()
                else:
                    ser.port = '/dev/ttyACM' + str(i-5)
                    ser.open()
                    list.append('/dev/ttyACM' + str(i-5))
                    ser.close()
            except Exception as e:
                    print("Error open serial port" + str(e))
    elif sys.platform == 'darwin':
        print("No version for MAC")         
    if len(list) > 0:
        print("\nList of available ports:\n")
        print(list)
    else:
        print("\nThere is no available port!\n")
    return list


def serial_send(port,baudrate,data="1",counter=1,
    parity=serial.PARITY_NONE,size=serial.EIGHTBITS,
    stop=serial.STOPBITS_TWO):
    
    ser = serial.Serial()
    ser.port = port
    ser.baudrate = baudrate
    ser.parity = parity
    ser.bytesize = size
    ser.stopbits = stop
    try:
        ser.open()
        print("\nPort open!\n")
        for i in range(counter):
            ser.write(data[i])
            ser.close()
    except Exception as e:
        print("Error open serial port: " + str(e))
    

def serial_receive(port,baudrate,counter=1,p=True,
    parity=serial.PARITY_NONE,size=serial.EIGHTBITS,
    stop=serial.STOPBITS_TWO):
    
    ser = serial.Serial()
    ser.port = port
    ser.baudrate = baudrate
    ser.parity = parity
    ser.bytesize = size
    ser.stopbits = stop
    bufferSerial = []
    try:
        ser.open()
        if p:
            print("\nPort open!\n")
            for i in range(counter):
                bufferSerial.append(ser.read(1))
                ser.close()
    except Exception as e:
        print("Error open serial port: " + str(e))
    return bufferSerial


def serial_send_receive(port,baudrate,p=True,parity=serial.PARITY_NONE,
    size=serial.EIGHTBITS,stop=serial.STOPBITS_TWO,data="1"):
    
    ser = serial.Serial()
    ser.port = port
    ser.baudrate = baudrate
    ser.parity = parity
    ser.bytesize = size
    ser.stopbits = stop
    bufferSerial = 0
    try:
        ser.open()
        if p:
            print("\nPort open!\n")
        ser.write(data)
        bufferSerial = ser.read(1)
        ser.close()
    except Exception as e:
            print("Error open serial port: " + str(e))
    return bufferSerial

