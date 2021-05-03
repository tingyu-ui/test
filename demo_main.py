#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from time import sleep,ctime
logging.basicConfig(level=logging.INFO)

loops=[2,4]
def loop(nloop,nsec,lock):
    logging.info("start loop" + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + "at " + ctime())
    lock.release()




# def loop0():
#     logging.info("start loop0 at " + ctime())
#     sleep(4)
#     logging.info("end loop0 at " + ctime())

# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(2)
#     logging.info("end loop1 at " + ctime())

def main():
    logging.info("start all at " + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop, (i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():pass
    loggin.info("end all at " + ctime())
    # _thread.start_new_thread(loop0, ())
    # thread.start_new_thread(loop1, ())
    # sleep(6)
    # logging.info("end all at " + ctime())

if __name__ == '__main__':x
    main()
