import threading
from threading import Thread
from time import sleep


def simple_worker():
    print('hello\n')


t1 = Thread(target=simple_worker)
t1.start()
print(t1.getName())
print(t1.ident)
print(t1.is_alive())


print(threading.active_count())
th1=threading.current_thread() #returns current thread
thId=threading.get_ident() # return current thread ID

threading.enumerate() # list of alive threads
#The list includes daemon threads, dummy thread objects created by current_thread() and the main thread

mainThread=threading.main_thread() # returns main thread



'''def worker():
    for i in range(0, 10):
        print('.', end='', flush=True)
        sleep(1)


print('Starting')

# Create read object with reference to worker function
t = Thread(target=worker)

# Start the thread object
t.start()

# Wait for the thread to complete
t.join()
print('\nDone')'''

def worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
print('Starting')
t1 = Thread(target=worker,name='thread 1', args='A') # arguments must be a tuple
t2 = Thread(target=worker,name='thread 2', args='B')
t3 = Thread(target=worker, args='C')
t1.start()
t2.start()
t3.start()
print('Done')

print(threading.active_count())
th1=threading.current_thread() #returns current thread
thId=threading.get_ident() # return current thread ID
print(th1.name , thId)
print(threading.enumerate()) # list of alive threads
#The list includes daemon threads, dummy thread objects created by current_thread() and the main thread

mainThread=threading.main_thread()
print(mainThread.ident)


class WorkerThread(Thread):
    def __init__(self,daemon=None,target=None , name=None):
        super().__init__(daemon=daemon,target=target,name=name)

    def run(self):
        for i in range(0, 10):
            print('.', end='', flush=True)
            sleep(1)

print('Starting')
t = WorkerThread()
t.start()
print('\nDone')

### daemon thread
def worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
print('Starting')
# Create a daemon thread
d = Thread(daemon=True, target=worker, args='C')
d.start()
sleep(5)
print('Done')

from threading import Timer
def hello():
    print('hello')
print('Starting')
t = Timer(5, hello)
t.start()
print('Done')

from threading import Thread, local, currentThread
from random import randint


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        print(currentThread().name, ' : No value yet')
    else:
        print(currentThread().name, ' : value =', val)


def worker(data):
    show_value(data)
    data.value = randint(1, 100)
    show_value(data)


print(currentThread().name, ' : Starting')
local_data = local()
show_value(local_data)
for i in range(2):
    t = Thread(name='W' + str(i), target=worker, args=[local_data])
    t.start()
show_value(local_data)
print(currentThread().name, ' : Done')
