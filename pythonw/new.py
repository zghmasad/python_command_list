
import turtle
#_________________________________________________________
IMAGE_SIZE_Y=500
IMAGE_SIZE_X=500
MAX_Y=500
MAX_X=500
MIN_X=10
MIN_Y=10
SCREEN_OFFSET_X=25
SCREEN_OFFSET_Y=25
MAX_ITERATIONS=5

for y in range(IMAGE_SIZE_Y):
    zy = y * (MAX_Y - MIN_Y) / (IMAGE_SIZE_Y - 1) + MIN_Y
    for x in range(IMAGE_SIZE_X):
        zx = x * (MAX_X - MIN_X) / (IMAGE_SIZE_Y - 1) + MIN_X
        z = zx + zy * 1j
        c = z
        for i in range(MAX_ITERATIONS):
            if abs(z) > 2.0:
                break
            z = z * z + c
        turtle.color((i % 4 * 64, i % 8 * 32, i % 16 * 16))
        turtle.speed(10)
        turtle.setposition(x - SCREEN_OFFSET_X,
        y - SCREEN_OFFSET_Y)
        turtle.pendown()
        turtle.dot(1)
        turtle.penup()

#_______________________________________________________________
import turtle
# Set up Constants
ANGLES = [60, -120, 60, 0]
SIZE_OF_SNOWFLAKE = 300
def get_input_depth():
    """ Obtain input from user and convert to an int"""
    message = 'Please provide the depth (0 or a positive interger):'
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer!')
        value_as_string = input(message)
    return int(value_as_string)
def setup_screen(title, background='white', screen_size_x=640,
screen_size_y=320, tracer_size=800):
    print('Set up Screen')
    turtle.title(title)
    turtle.setup(screen_size_x, screen_size_y)
    turtle.hideturtle()
    turtle.penup()
    turtle.backward(240)
    # Batch drawing to the screen for faster rendering
    turtle.tracer(tracer_size)
    turtle.bgcolor(background) # Set the background colour of the screen

def draw_koch(size, depth):
    if depth > 0:
        for angle in ANGLES:
            draw_koch(size / 3, depth - 1)
            turtle.left(angle)
    else:
        turtle.forward(size)
depth = get_input_depth()
setup_screen('Koch Snowflake (depth ' + str(depth) + ')',
background='black',
screen_size_x=420, screen_size_y=420)
# Set foreground colours
turtle.color('sky blue')
# Ensure snowflake is centred
turtle.penup()
turtle.setposition(-180,0)
turtle.left(30)
turtle.pendown()
# Draw three sides of snowflake
for _ in range(3):
    draw_koch(SIZE_OF_SNOWFLAKE, depth)
    turtle.right(120)
# Ensure that all the drawing is rendered
turtle.update()
print('Done')
turtle.done()
#_____________________________________________________

import fileinput
import glob

with open('test.xml', 'r+') as f:
    print(f.name)
    print(f.mode)
    print(f.closed)
print(f.closed)


with fileinput.input(files=('test.xml','test2.xml')) as f:
    print(f.filename())
    print(f.isfirstline())
    print(f.lineno())
    print(f.filelineno())
    for i in f:
        print(i,end='')

print('\n______________________________________')
with fileinput.input(files=('test.xml','test2.xml')) as f:
    line=f.readline()
    print(line)

import os
#os.rename('test.xml','t.txt')
#os.remove('somefilename.txt')
#os.rmdir('dirurl')
print(os.listdir())#returns a list of all files and folders

#f.seek(offset, whence)   ####
#هر وقت پارامتر دوم 0 باشد به معنی آفست از اول فایل است و اگر 1 باشد به معنی از مکان جاری کرسر و اگر 2 باشد به معنی آفست از آخر


import tempfile
print('tempfile.gettempdir():', tempfile.gettempdir())
temp = tempfile.TemporaryFile('w+')
print('temp.name:', temp.name)
print('temp.mode:', temp.mode)
temp.write('Hello world!')
temp.seek(0)
line = temp.readline()
print('line:', line)

from pathlib import Path
print('Create Path object for current directory')
p = Path('.')
p2 = Path(r'c:\Users')
print('p:', p)  #
print('p.exists():', p.exists()) # check dir exists()
print('p.is_dir():', p.is_dir()) # check the path is dir or not
print('p.is_file():', p.is_file()) # chek the path is file or not
print('p.absolute():', p.absolute())  # print(os.getcwd())

p = Path.cwd()
print('Set up new directory')
newdir = p / 'test'
print('Check to see if newdir exists')
print('newdir.exists():', newdir.exists())
print('Create new dir')
if(not newdir.exists()):
    newdir.mkdir()
print('newdir.exists():', newdir.exists())

c=newdir/'temp3'
print('c is this:', c)
c=newdir.joinpath('temp3')
print('c is this:', c)

try:
    newdir.rmdir()
except WindowsError as e:
    print(e)

p = Path('./new.py')
for i in p.glob('*'):
    print(i)

print(newdir.name)
