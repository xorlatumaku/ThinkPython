# Date: 06/11/2025
# Program to implement programmer-defined types

class Time:
    """ Represents a time of day. """

lunch = Time()
print(type(lunch))

lunch.hour = 11
lunch.minute = 59
lunch.second = 1

print(lunch.hour)
print()

total_minutes = lunch.hour * 60 + lunch.minute
print(total_minutes)
print()

print(f'{lunch.hour}:{lunch.minute}:{lunch.second}')
print()

print(f'{lunch.hour}:{lunch.minute:02d}:{lunch.second:02d}')
print()

def print_time(time):
    s = f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}'
    print(s)
print_time(lunch)
print()

# Objects as Return Values
def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time
time= make_time(11, 59, 1)
print_time(time)
print()

# Objects are mutable
start = make_time(9, 20, 0) # Start time
print_time(start)
print()

start.hour += 1 # end time
start.minute += 32
print_time(start)
print()

def increment_time(time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds

start = make_time(9, 20, 0)
increment_time(start, 1, 32, 0)
print_time(start)
print()

# Copying module provides a function called copy
from copy import copy
start = make_time(9, 20, 0)
end = copy(start)
print_time(start)
print_time(end)
print(start is end)
print()

# Pure Functions
def add_time(time, hours, minutes, seconds):
    total = copy(time)
    increment_time(total, hours, minutes, seconds)
    return total
end = add_time(start, 1, 32, 0)
print_time(end)
print_time(start)
print()

#  Prototype and Patch
start = make_time(9, 40, 0)
def increment_time(time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
end = add_time(start, 1, 32, 0)
print_time(end)
print()

end = copy(start)
end.minute = start.minute + 92
print(end.minute)

carry, end.minute = divmod(end.minute, 60)
print(carry, end.minute)
end.hour += carry
print_time(end)
print()

def increment_time(time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds

    carry, time.second = divmod(time.second, 60)
    carry, time.minute = divmod(time.minute + carry, 60)
    carry, time.hour = divmod(time.hour + carry, 60)

end = add_time(start, 0, 90, 120)
print_time(end)

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

time = make_time(1, 1, 1)
print_time(time)
time_to_int(time)

def int_to_time(seconds):
    minute, second = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    return make_time(hour, minute, second)
time = int_to_time(3661)
print_time(time)
print()

def add_time(time, hours, minutes, seconds):
    duration = make_time(hours, minutes, seconds)
    seconds = time_to_int(time) + time_to_int(duration)
    return int_to_time(seconds)
start = make_time(9, 40, 0)
end = add_time(start, 1, 32, 0)
print_time(end)
