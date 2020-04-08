import multiprocessing
import os
from time import sleep


def worker(msg):
    print('process id:', os.getpid())
    for i in range(0, 10):
        print(msg, end='')
        sleep(1)

print('Starting')
if __name__=='__main__':
    print('process id:', os.getpid())
    ctx = multiprocessing.get_context('spawn')
    p = ctx.Process(target=worker, args=('A',))
    '''or p = Process(target=worker, args=('A',),name='ali')'''
    p.start()

print('Done')