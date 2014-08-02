#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process

""" определяем что будет делать воркер """
def handler(n):
    while n > 0:
        n -= 1
        print n

""" рутовый процесс. запускаем воркера 
и передаем ему аргумент который он будет пилить. """
if __name__ == '__main__': 
    worker = Process(target=handler, args=(100000000,))
    worker.start()
    worker.join()