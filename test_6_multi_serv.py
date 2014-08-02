#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing
import socket

def worker(connections, address):
    try:
        print "Connected at %r" % (address)
        data = 1
        while True:
            data = connections.recv(1024)
            if data == "":
                print "Connecting closed: remote"
                break
            print "%r Recv: %r" % (address, data)
            connections.send(data.upper())
            print "%r Send: %r" % (address, data.upper())
    except Exception, e:
        print 'Problem recv:', e
    finally:
        print "%r Closing socket" % (address)
        connections.close()

class master:
    def __init__ (self, bindIP, bindPort, timeout):
        self.host = bindIP
        self.port = bindPort
        self.timeout = timeout
        print "Server config for master process: \n Bind IP %r \n Bind port: %r \n Connect timeout: %r" % (self.host, self.port, self.timeout)

    def upSocket(self):
        # Инициируем сокет и цепляемся на порт
        print "Binding port %r" % (self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port)) 
        self.sock.listen(1)

            # Ловим коннект, устанавливаем таймаут.
            # Создаем чилдовый процесс таргет функция worker
            # и запускаем его.
        while True:
            print "Listen for new connections"
            conn, addr = self.sock.accept()
            conn.settimeout(self.timeout)
            print "connected: %r %r" % (str(addr), str(conn))
            ChildProcess = multiprocessing.Process(target=worker, args=(conn, addr))
            ChildProcess.daemon = True
            ChildProcess.start()
            print "Started process %r" % (ChildProcess)


if __name__ == '__main__':
    # Запускаем обьект и определяем его свойства
    # В дальнейшем предполагается хавать параметры из конфига
    HOST, PORT, TIMEOUT = "0.0.0.0", 9005, 60

    MasterProcess = master(HOST,PORT,TIMEOUT)
    try:
        MasterProcess.upSocket()
    except Exception, e:
        print 'Error:', e
    finally:
        for ChildProcess in multiprocessing.active_children():
            print "Shutting down process %r" % (ChildProcess)
            ChildProcess.terminate()
            ChildProcess.join()
    print "Service has stopped"