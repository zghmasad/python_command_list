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

from multiprocessing import Pool
from time import sleep


def worker(x):
    print('In worker with: ', x)
    sleep(3)
    return x * x


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        print(pool.map(worker, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__== '__main__':
    with Pool(processes=4) as pool:
        for result in pool.imap_unordered(worker,[1,2,3,4,5,6,7,8,9]):
            print(result)