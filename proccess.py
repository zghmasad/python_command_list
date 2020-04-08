import os
from multiprocessing import Process
from time import sleep



def worker(msg):
    print('process id:', os.getpid())
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)

print('Starting')
if __name__=='__main__':
    print('process id:', os.getpid())
    t2 = Process(target=worker, args=('A',),name='ali')
    t2.start()
print('Done')
