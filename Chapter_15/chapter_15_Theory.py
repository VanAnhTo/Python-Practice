import time
import datetime
#The datetime Module

'''
print(datetime.datetime.now())

dt = datetime.datetime(2018, 1 , 22, 20, 59, 10)

print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)
'''

#The timedelta Data Type
'''
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)

print(delta.total_seconds())
print(str(delta))
'''
dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)


