#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import socket

""" определяем что будет делать воркер """
def handler(connection, address):
		# работаем в цикле пока есть данные если нет то выход из цикла
        while True:
            data = connection.recv(1024)
            if data == "":
                break
            connection.send(data.upper())

		# Если цикл оборвался тушим коннект            
        connection.close()

""" рутовый процесс. запускаем воркера 
и передаем ему аргумент который он будет пилить. """
if __name__ == '__main__': 

	host = "0.0.0.0"
	port = 9091
	timeout = 30
	# Инициируем сокет и цепляемся на порт
	sock = socket.socket()
	sock.bind((host, port)) 
	sock.listen(1)

	while True:
		# ловим коннект
		conn, address = socket.accept()
		conn.settimeout(timeout)

		# запускаем чилда
    	worker = Process(target=handler, args=(conn, address))
    	worker.daemon = True
    	worker.start()
    	worker.join()

    #for worker in multiprocessing.active_children():
    	#print "Тушим процессы %r" % worker
     	#worker.terminate()
     	#worker.join()
    #print "Работа завершена"