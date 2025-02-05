from datetime import datetime
someday = datetime(2016,9,16,22,33,32,7)
print(someday.strftime("%Y-%m-%d  %H:%M:%S"))
print(someday.strftime("%x  %H:%M:%S "))
print(someday.strftime("%A, %B %d, %Y %I:%M %p"))
print(someday.strftime("%X %x"))
print(someday.strftime("%Y %B %d %X"))
