#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

class master:
    def __init__ (self, bindIP, bindPort, timeout):
        self.host = bindIP
        self.port = bindPort
        self.timeout = timeout
        print "Server config for master process: \n Bind IP %r \n Bind port: %r \n Connect timeout: %r" % (self.host, self.port, self.timeout)

    def upSocket(self):
        # Инициируем сокет и цепляемся на порт
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port)) 
        self.sock.listen(1)

        # Ловим коннект
        conn, addr = self.sock.accept()
        print 'connected: %r %r' % (str(addr), str(conn))
    
        # установка таймаута
        conn.settimeout(self.timeout) 

        # Работаем с данными туда-сюда
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print "%r %r Recv: %r" % (str(addr),str(conn),data)
            conn.send(data.upper())
            print "%r %r Send: %r" % (str(addr),str(conn),data.upper())
        conn.close()


if __name__ == '__main__':
    # Запускаем обьект и определяем его свойства
    # В дальнейшем предполагается хавать параметры из конфига
    HOST, PORT, TIMEOUT = "0.0.0.0", 9005, 120

    MasterProcess = master(HOST,PORT,TIMEOUT)
    try:
        MasterProcess.upSocket()
    except Exception, e:
        print 'Error:', e
    #finally:
        #conn.close()