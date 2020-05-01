import decimal
import json
from collections import deque
from datetime import datetime
import turtle
import sys
from math import pi

year = 1990
month = 11
day = 12
hour = 12
second = 30
minute = 11
if 1900 < year < 2100 and 1 <= month <= 12 \
        and 1 <= day <= 31 and 0 <= hour < 24 \
        and 0 <= minute < 60 and 0 <= second < 60:  # Looks like a valid date
    print('this date is valid')

# implicit line join
month_names = ['Januari', 'Februari', 'Maart',  # These are the
               'April', 'Mei', 'Juni',  # Dutch names
               'Juli', 'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']  # of the year

# keywords
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

# integers--------------------------------------------------
int1 = 2147483647
print(int1)
long1 = 79228162514264337593543950336
print(long1)
underlined_int = 100_000_000_000
print(underlined_int)
octal1 = 0o177
print(octal1)
print(type(octal1))
binary1 = 0b_1110_0101
print(binary1)
hexadecimal1 = 0xdeadbeef
print(hexadecimal1)

# floor of a division
print("floor of two int", underlined_int // int1)

# remain of a division
print("remain of to int", underlined_int % int1)

# power
print("power of two int", 4 ** 8)

# floating points--------------------------------------------

float1 = 3.14
print(float1)
float1 = 10.
print(float1)
float1 = .001
print(float1)
float1 = 1e100
print(float1)
float1 = 3.14e-10
print(float1)
float1 = 0e0
print(float1)
float1 = 3.14_15_93
print(float1)

# round
print('round of 13.14546 is:', round(13.14546, 2))

# اعداد موهومی--------------------------------------------------
imaginary1 = 3.14j
print(imaginary1)
imaginary1 = 10.j
print(imaginary1)
imaginary1 = .001j
print(imaginary1)
imaginary1 = 1e100j
print(imaginary1)
imaginary1 = 3.14e-10j
print(imaginary1)
imaginary1 = 0e0j
print(imaginary1)
imaginary1 = 3.14_15_93j
print(imaginary1)

# strings---------------------------------------------------------
name = "Fred"
print(f"He said his name is {name!r}.")  # add a single quotation
print(f"He said his name is {name}.")
print(f"He said his name is {repr(name)}.")  # add a single quotation
print(f"He said his name is {name.upper()}")  # .lower is the lowercase func
print()
# strings index
print(name[0])
print(name[-1])  # last character
print(name[-4])  # first character
print(name[0:2])  # Fre
print(name[:2] + name[2:])  # name[0:2]+name[2:last]
print(name[-2:])  # name[last-1:last]
print(len(name))  # length of name

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")  # تعیین طول و دقت عدد
today = datetime(year=2017, month=1, day=27)
print(f"{today:%B %d, %Y}")  # فرمت تاریخ
number = 1024
print(f"{number:#0x}")  # hexadecimal
newline = ord('\n')
print(f"newline: {newline}")  # new line ord
newline = ord('\a')
print(f"newline: {newline}")  # new line ord

# quotation
print('this is single quotation example', 'doesn\'t')
print('this is single quotation example', "\"yes\" they said.")
print('this is double quotation example', "doesn't")
print('this is double quotation example', '"yes" they said.')

# \n delimiter
print('this is \\n delimiter example', 'C:\some\name')
print('this is \\n delimiter exampler', r'C:\some\name')

# triple quot example
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# plus and time(cross) operators on string
print('this is plus and time operators on strings: ', 5 * 'ui' + 'tr')

# string concatenation
print('strings concat with space: ', 'Py' 'thon')
print('strings concat with plus: ', 'Py' + 'thon')


# formatted strings cannot use as function document
def foo():
    f"Not a docstring"


print(foo.__doc__ is None)

#  format strings
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

print(vars())  # returns a dictionary containing all variables

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d} {3:5d}'.format(x, x * x, x * x * x, x * x * x * x))

# equals to
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x * x * x).rjust(4), end=' ')
    print(repr(x * x * x * x).rjust(5))

# zfill()
print('12'.zfill(5))
print('-12.34'.zfill(7))
print('-12.34'.zfill(2))

# flow controls
# if--------------------------------------------------------------------------------

b = 3
a = 2
c = 1
if b > 0:
    print(a)
elif b < 0:
    print(b)
else:
    print(c)

# for-------------------------------------------------------------------------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# foreach
for letter in letters:
    print(letter)

for letter in letters.copy():
    if letter == 'a':
        letters.append('x')

print(letters)

# range function
print('range(5)')
for i in range(5):
    print(i)

print('range(5, 10)')
for j in range(5, 10):
    print(j)

print('range(0, 10, 3)')
for j in range(0, 10, 3):
    print(j)

print('range(-10, -100, -30)')
for k in range(-10, -100, -30):
    print(k)

for i in range(len(letters)):
    print(i, letters[i])

# sum and list on range
print(sum(range(4)))
print(list(range(4)))

# break and else for a 'for loop'
for n in range(2, 100):
    t = n // 2
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# continue
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


# pass
# an endless loop
# while True:
# pass

def initlog(*args):
    pass  # Remember to implement this!


# unpacking args-----------------------------------------------------
list(range(3, 6))  # [3, 4, 5]
args = [3, 6]
list(range(*args))  # [3, 4, 5]


# lambda ------------------------------------------------------------
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))


def powerto10(n):
    return lambda x: x ** n


f = powerto10(10)
print(f(2))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
pairs.sort(key=lambda pair: len(pair[1]))
print(pairs)
pairs.sort(key=lambda pair: pair[0])
print(pairs)

a = [10, 'number', 11.2]
a.sort(key=lambda x: x.__class__.__name__)
print(a)


# functions----------------------------------------------------------
def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(2000)
func = fib
func(2000)


# default arguments
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    ok = input(prompt)  # input
    if ok in ('y', 'ye', 'yes'):
        return True
    if ok in ('n', 'no', 'nop', 'nope'):
        return False
    retries = retries - 1
    if retries < 0:
        raise ValueError('invalid user response')
    print(reminder)


ask_ok('are you ok', 2, 'ok error')


def f(a, L=[]) -> str:
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

print(f.__annotations__)

# List-------------------------------------------------------
# cut a list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[2:5])
letters[2:5] = []
print(letters)
print(len(letters))
# nested lists
x = [['a', 'b', 'c'], [1, 2, 3]]
print(x)
print(x[1])
print(x[1][1])
# swap to or more variables
a, b, c = 1, 2, 3
print(a, b, c)
a, b, c = b, c, a
print(a, b, c)

squares = [1, 4, 9, 16, 25]
print(squares, squares[4])
print(squares[-3:])  # prints 9, 16, 25
print(squares + [36, 49, 64, 81, 100])  # prints 1,4,9,...,100
# strings are immutable and we can't change name[i]
# but lists are mutable and we can change squares[i]

squares.append(36)
letters.clear()  # removes all items
print(letters)
letters.extend(['1', '2', '3'])  # equals to letters[len(letters):]=['1','2','3']
print(letters)
letters.insert(3, 'o')
letters.append('r')
letters.remove('2')
print(letters)
letters.pop()  # removes last item and returns it
print(letters)
letters.pop(2)  # removes item with index 2 and returns it
print(letters)

print(letters.count('1'))  # returns count of '1'
print(letters.index('1'))  # returns index of '1'
print(letters.index('1', 0, 4))  # returns index of '1' in letters[2:4] if exists

letters.reverse()  # reverses the order of elements
letters.sort()  # sorts the elements
letters.copy()  # copies the list

print(letters[0:4:2])  # third part indicates step count

# stack
# use a list as stack with functions pop() and append()

# queue
queue = deque(["Eric", "John", "Michael"])  # do not forget to import collections.deque
queue.append('ali')
queue.popleft()
print(queue)

# list comprehensions
squares2 = list(map(lambda rr: rr ** 2, range(10)))
print(squares2)

squares3 = [x ** 2 for x in range(10)]
print(squares3)

combos = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combos)

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)

vector = [2, 1, -2, 5]
vector2 = [x * 2 for x in vector]
vector3 = [x for x in vector if x >= 0]
vector4 = [abs(x) for x in vector]
print(vector2)
print(vector3)
print(vector4)

freshFruit = ['  banana', '  loganberry ', 'passion fruit  ']
temp = [weapon.strip() for weapon in freshFruit]  # you can call a function on each element
print(temp)

temp = [(x, x ** 2) for x in range(6)]  # you can create a two tuples
print(temp)

# flatten a 2d list
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

# complex expressions and nested functions
print([str(round(pi, i)) for i in range(1, 6)])

# zip() function - zip function
x = [1, 2, 3]
y = [4, 5]
z = [6, 7, 8, 9]
print(list(zip(x, y, z)))

# nested list comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

transp = []
for i in range(4):
    transp.append([row[i] for row in matrix])  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

print(transp)

print(list(zip(*matrix)))

# del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a
# print(a) error occurs

# tuples--------------------------------------------------
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)

# t[0] = 88888 ## occurs an error because tuples are immutable
v = ([1, 2, 3], [3, 2, 1])
print(v)
v[1][1] = 1  # doesn't occur an error because tuples can take immutable objects
print(v[1][1])

empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
t = 12345, 54321, 'hello!'
x, y, z = t
print(z)

# Sets---------------------------------------------------
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)  # fast membership testing

print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)  # unique letters in a
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both

# Similarly to list comprehensions, set comprehensions are also supported
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# Dictionaries---------------------------------------------
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
list(tel)
sorted(tel)
print('guido' in tel)
print('jack' not in tel)
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
newdict = {x: x ** 2 for x in (2, 4, 6)}
print(newdict)
newdict = dict(sape=4139, guido=4127, jack=4098)
print(newdict)

# files--------------------------------------------
# with means open file and after end close
with open('workfile') as f:  # read entire file 'workfile' 'r' tag for read
    print(f.tell())  # returns the position of the cursor
    # f.seek(offset, whence)
    print(f.seek(12))  # seek the cursor to giving position
    read_data = f.read()
    print(f.tell())
    read_data2 = f.read()  # returns empty string
    print(read_data)
    print(read_data2)
    # print(f.seek(-3))

print(f.close())
print('///')

# read line
with open('workfile') as f:
    for line in f:  # read line of a file 'workfile' is dir
        print(line, end='')  # end='' is for preventing of end-of-line
# f.close()

# write
with open('workfile', 'w') as f:  # 'w' tag for write 'x' for exec 'a' for append
    # https://docs.python.org/3/library/functions.html#open
    f.write('This is a test\n')

# json--------------------------------------------------

print(json.dumps([1, 'simple', 'list']))
x = json.dumps([1, 'simple', 'list'])
with open('workfile', 'w') as f:
    json.dump(x, f)

with open('workfile', 'r') as f:
    x = json.load(f)

print(x)

yd = json.dumps({'ali': 'saifi', 'mohsen': 'saifi'})
print(yd)


# namespaces ---------------------------------------------
# global means in global scope
# nonlocal means in enclosing scope نزدیک ترین والد
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


# classes----------------------------------------------
class MyClass:
    """A simple example class"""
    staticVar = 2  # static object

    def f(self):
        return 'hello world'

    # static example
    @staticmethod
    def f2():
        return 'hello world'

    def printPrivate(self):
        print(self._privatevalue)

    def __init__(self, tempList):
        self.data = tempList
        self.i = 12345
        self._privatevalue = 2  # private value starts with '_'

    # def __init__(self):
    #     self.data = [0, 0]


x = MyClass([1, 2])
print(x.i)
print(x.f())
x.printPrivate()
print(x.data)
del x.data


# print(x._privatevalue)


# print(x.data) this will raise an error


# Function defined outside the class
def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


c = C()
print(c.f(1, -1))
print(c.h())


class D(C):
    data2 = 'this is inheritance'


d = D()
print(d.g())


class GG(C, MyClass):
    def __init__(self):
        g = 0

    def g(self):  # overrides C.g()
        return 'hello world2'


gg = GG()
print(gg.g())


# Structure --------------------------
class Employee:
    pass


john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print(john.salary)

# iterators
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one': 1, 'two': 2}:
    print(key)
for char in "123":
    print(char)
for line in open("workfile"):
    print(line, end='')

s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


for char in Reverse('spam'):
    print(char)


# generators
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

# Generator expressions
sum(i * i for i in range(10))
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x * y for x, y in zip(xvec, yvec))
data = 'golf'
list(data[i] for i in range(len(data) - 1, -1, -1))

# turtle----------------------------------------------------
# turtle.color('red', 'yellow')
# turtle.begin_fill()
# while True:
#     turtle.forward(200)
#     turtle.left(170)
#     if abs(turtle.pos()) < 1:
#         break
# turtle.end_fill()
# turtle.done()

# Exception handling ------------------------------------------
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except (RuntimeError, TypeError, NameError, ValueError):
        print("Oops!  That was no valid number.  Try again...")
        print()


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# else statement in try runs if no exception 'it is very useful really'
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# raise statement
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,


# finally example
def bool_return():
    try:
        return True
    finally:
        return False


print(bool_return())
try:
    raise NameError('HiThere')  # this raises an exception
except NameError:
    print('An exception flew by!')
    raise
