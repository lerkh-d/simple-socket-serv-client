#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

HOST = "localhost"
PORT = 9005
sock = socket.socket()

def connect_to_server():
    print "Connecting to %r: %r" % (HOST, PORT)
    try :
        sock.connect((HOST, PORT))
    except Exception, e:
        print "Connecting failed, exception:", e
        return
    print "Connect: Establish"

connect_to_server()

# sock.connect(('localhost', 9090))

while 1:
	input_text = raw_input("Send: ")
	if input_text == "" or input_text == "quit" or input_text == "q":
		break

	sock.send(input_text)

	data = sock.recv(1024)
    #if srt(data) == "Com:close":
    #     print "Resv:[Com:close]"
    #     print "Connect: Close"
    #     break
	print "Resv: " + data

sock.close()
