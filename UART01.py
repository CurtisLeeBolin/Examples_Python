#!/usr/bin/python
# uart-eg01.py
#
# to run on the other end of the UART
# screen /dev/ttyUSB1 115200

import serial

def readlineCR(uart):
	line = b''
	while True:
		byte = uart.read()
		line += byte
		if byte == b'\r':
			return line

uart = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=1)

while True:
	uart.write(b'\r\nSay something: ')
	line = readlineCR(uart)
	if line != b'exit\r':
		lineStr = '\r\nYou sent     : {}'.format(line.decode('utf-8'))
		uart.write(lineStr.encode('utf-8'))
	else:
		uart.write(b'\r\nexiting\r\n')
		uart.close()
		exit(0)
