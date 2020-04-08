from datetime import date, datetime
import zlib

# datetime-------------------------------------------------
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1987, 7, 31)
birthday2 = datetime(1987, 7, 31)
x = now - birthday
print(str(x.days // 365) + ' years')

s = b'witch which has which witches wrist watch'
s3 = 'witch which has which witches wrist watch'
print(type(s))

# compression------------------------------------------------
t = zlib.compress(s)
print(t)
s2 = zlib.decompress(t)
print(s == s2)
print(s2)
print(type(s2))
print(s)
print(zlib.crc32(s))

# Timer------------------------------------------------------
from timeit import Timer

traditional_swap_time = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

print(traditional_swap_time)
tuple_unpacking_swap_time = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(tuple_unpacking_swap_time)

print(Timer('a**b', 'a=5;b=26').timeit())
print(Timer('a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a', 'a=5;').timeit())

# Test Example------------------------------------------------------
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()
def power2(base, power3):
    """
    >>> print(power2(3,5))
    243
    """
    x = base
    for i in range(power3-1):
        x = base * x

    return x


import doctest

doctest.testmod()

# strings split and list join-------------------------------
strings='problem1, problem2, problem3, problem4, problem5, problem6'
list1=strings.split(', ')
print(list1)
print(' and '.join(list1))
