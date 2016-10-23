#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  serial.py
#  
#  Copyright 2014 Nikhil <nik@encypher>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import serial
import socket , sys
import os
import time				
port_a = 30003				
ip = 'localhost'			
#ser = serial.Serial('/dev/ttyACM0', 9600)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)       # For  creating the  UDP server 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	   #  For resuing  the  port  again 

MAX = 65535



def write_server(x , a , z):
	#s.sendto(x)
	s.sendto( x , ( a , z))
	print "sending.. \n"
	

def read_server(y , a , z):
	s.sendto(y , ( a , z))
#	s.send(y)

	print "sending.. \n"

#############################################################################

if sys.argv[1:] == ['server']:
#	port= raw_input("please  enter the  port: ")
#	PORT = int(port )
#	ip= raw_input("please  enter the  IP: ")
	s.bind((ip , port_a))
	print 'Listining  at' ,  s.getsockname()
	while True:
		new_update , address = s.recvfrom(MAX) 
		print new_update
		if(new_update == "move_right"):
			print 'working 1'
		#	ser = serial.Serial("/dev/ttyUSB0",9600)
			ser.write("b")
		#	ser.close()
		if(new_update == "move_left"):
			print 'working 2'
		#	ser = serial.Serial("/dev/ttyUSB0",9600)
			ser.write("x")
		#	ser.close()
		if(new_update == "move_frwd"):
			print 'working 3'
		#	ser = serial.Serial("/dev/ttyUSB0",9600)
			ser.write("c")
		#	ser.close()
		if(new_update == "move_back"):
			print 'working 4'
		#	ser = serial.Serial("/dev/ttyUSB0",9600)
			ser.write("y")
		#	ser.close()
		if(new_update == "room1:switch3:on"):
			print 'working 5'
		#	ser = serial.Serial("/dev/ttyUSB0",9600)
		#	ser.write("d")
		#	ser.close()
		if(new_update == "room1:switch3:off"):
			print 'working 6'
		#	ser = serial.Serial("/dev/ttyUSB0",9600)
		#	ser.write("w")
		#	ser.close()
		if(new_update == "room1:switch4:on"):
			print 'working 7'
		#	ser = serial.Serial("/dev/ttyUSB0",9600)
		#	ser.write("e")
		#	ser.close()
		if(new_update == "room1:switch4:off"):
			print 'working 8'
		#	ser = serial.Serial("/dev/ttyUSB0",9600)
		#	ser.write("v")
		#	ser.close()					
	#	
	

#	while True:
#		new_data = ser.read(5)
#		s.sendto('tmp:'+new_data , address)
		
		 
		
	
		
		
###########################################################################################################		
		
elif sys.argv[1:] == ['client']:
	print "This  program is  for basic testing of socket server and  responce  " + '\n'
#	port=     #raw_input("please  enter the  port: ")
	PORT = 9999   #int(port )
	PORT1 = 9991
	ip='192.168.1.7'     #raw_input("please  enter the  IP: ")
	#while (1) :
	server_data = ()
	
	fo = open("stt.txt", "r+")
#	lines = (line.strip('\n') for line in open('stt.txt' ))
	st = fo.read();
	line = st.strip('\n')
	print "Read String is : ", line
	if (line == 'play'):
		write_server(line , ip , PORT  )
	if (line == 'play sweet'):
			write_server(line , ip , PORT  )
	if (line == 'stop'):
		write_server(line , ip , PORT  )		
	else:
		write_server(line , ip , PORT1 )
			
		
	# Close opend file
	fo.close()
	
	'''	
		user_data = raw_input("please  enter write  or read: ")
		print "\n"
		if (user_data == "write"):
			com_data = raw_input("please enter the name of the item: ")
			print "\n"
			server_data = ( user_data , com_data )
			send_data = ":".join(server_data)
			write_server(send_data , ip , PORT)
			print "Data is  sent  to server : " + send_data + "\n"
			msg = s.recvfrom(MAX) 

			print " server msg is " + repr(msg) + '\n'
			
		elif (user_data == "read"):
			com_data = raw_input("please enter the name of the item : ")
			print "\n"
			server_data = ( user_data , com_data )
			send_data = ":".join(server_data)
		#	s.send(send_data)
			read_server(send_data , ip , PORT)
			print "Data is  sent  to server :" + send_data + "\n"
			msg = s.recvfrom(MAX) 
			print " server msg is " + repr(msg) + '\n'
			
		else:
			print "please enter the  right command" + '\n'
	'''
	'''
	print 'Address before sending : ' ,  s.getsockname()
	s.sendto('This  is my message' , ('127.0.0.1' , PORT))
	print 'Address after sending ' , s.getsockname()
	data , address = s.recvfrom(MAX) 
	print 'The server ' , address ,  'says',  repr(data)
	'''
else:
	print  >>sys.stderr , 'usage: checked_udp.py server|client'

			
		
