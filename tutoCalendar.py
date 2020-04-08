import calendar
print(calendar.weekheader(2))  # returns weekheader with length 2
print(calendar.firstweekday())  # prints 0 for monday
print(calendar.month(2020, 1))  # returns calendar of a month in calendar format
print(calendar.monthcalendar(2020, 1))  # returns calendar of a month in list format
print(calendar.calendar(2020))  # returns calendar of a year in calendar format
for i in range(1, 12):  # returns calendar of a year in list format
    print(calendar.monthcalendar(2020, i))

print(calendar.weekday(2020, 2, 28))  # returns weekday of a date
print(calendar.isleap(2020))  # returns true if 2020 is leap year
print(calendar.leapdays(2000, 2021))  # not included 2021

