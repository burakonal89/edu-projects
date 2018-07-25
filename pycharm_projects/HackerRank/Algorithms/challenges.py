#!/bin/python

import sys


time = raw_input().strip().split(":")
hour = int(time[0])
minute = time[1]
second = time[2][:2]
string = time[2][2:]
if hour == 12:
    if string == "AM":
        hour += 12
elif string == "PM":
    hour += 12
hour = str(hour%24)
if len(hour) == 1:
    hour = "0"+hour
print "{0}:{1}:{2}".format(hour, minute, second)