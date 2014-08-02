#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

HOST = "0.0.0.0"
PORT = 9005
timeout = 120

# Инициируем сокет и цепляемся на порт
sock = socket.socket()
sock.bind((HOST, PORT)) 
sock.listen(10)

# Начинаем слушать
conn, addr = sock.accept()

print 'connected: ', addr
	
# установка таймаута
conn.settimeout(timeout) 

while True:
	# Начинаем слушать
	conn, addr = sock.accept()
	print 'connected: ', addr

   	data = conn.recv(1024)
   	if not data:
          conn.send("Com:close")
          print "Recv:[noDATA]"
          print "Com:close"
          break
   	print "Recv: " + data
   	conn.send(data.upper())
   	print "Send: " + data.upper()

conn.close()
exit
