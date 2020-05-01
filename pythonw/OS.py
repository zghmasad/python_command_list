import os
import shutil
import glob
import sys
import argparse
import re
import math
import random
import statistics

print(os.getcwd())  # get current dir
# make a directory
# os.system('mkdir today')
os.chdir('./today')  # change directory
print(os.getcwd())
print(dir(os))  # returns all module funcs
print(help(os))  # returns all module help
os.chdir('../../')
# copy a file
try:
    shutil.copyfile('workfile', 'archive.db')
except IOError:
    print('this file exists and not copied')
# move a file
try:
    shutil.move('archive.db', 'd:\\')
except IOError:
    print("this file exists and didn't moved")

os.chdir('d:\\')  # change directory
print(glob.glob('*.exe'))
print(sys.argv)  # arg[0] is the current executed file
print(sys.stderr.write('Warning, log file not found starting a new one\n'))
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
print('tea for too'.replace('too', 'two'))
print(math.cos(math.pi / 4))
print(math.log(1024, 2))
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())    # random float
print(random.randrange(6))    # random integer chosen from range(6)

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

parser = argparse.ArgumentParser(prog='top',
                                 description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
# python top.py --lines=5 alpha.txt beta.txt
list=args.filenames
for file1 in list:
    with open(file1) as f:
        for i in range(args.lines):
            print(f.readline(),end=' ')

sys.exit()  # exits from script
