import math
import calendar
import datetime

# print(dir(math))

# print(math.factorial(5))

# print(math.pow(2,2))
# print(pow(2,2))
# print(2**2)

# print(math.floor(35.29877841))
# print(math.floor(35.759877841))

# print(math.ceil(7.0001))
# print(math.ceil(7.4))

# print(math.sqrt(16))

# print(math.fabs(-7.3589))


# print(calendar.calendar(2005))

print(dir(datetime.datetime))
print(datetime.datetime.now())
print(datetime.datetime.now().date())
print(datetime.datetime.now().day)
print(datetime.datetime.now().month)
print(datetime.datetime.now().year)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)


from datetime import datetime
print(datetime.now())