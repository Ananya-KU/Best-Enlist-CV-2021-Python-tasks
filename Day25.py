# Date and Time in Python
# 1. Write a Python program to convert a string to datetime

import datetime

def convert(date_time):
    format = '%b %d %Y %I:%M%p' # The format
    datetime_str = datetime.datetime.strptime(date_time, format)
    return datetime_str

date_time = 'Mar 20 2020 01:20PM'
print(convert(date_time))

# 2. Write a Python program to subtract five days (last working day) from current date

from datetime import date, timedelta
delta = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date  is :',delta)

# 3. Write a Python program to convert the date to datetime using a function

from datetime import datetime
dt = date.today()
print(datetime.combine(dt, datetime.min.time()))

# 4. Write a Python program to print next 7 days (week) starting from today

import datetime
base = datetime.datetime.today()
for x in range(0, 7):
    print(base + datetime.timedelta(days=x))