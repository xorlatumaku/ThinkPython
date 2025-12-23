# Date: 06/12/2025
# Program to define methods
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
class Time:
    """ Represents the time of day. """
    def print_time(self):
        s = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        print(s)    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(seconds):
        minute, second = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)
        return make_time(hour, minute, second)

    def add_time(self, hours, minutes, seconds):
        duration = make_time(hours, minutes, seconds)
        seconds = time_to_int(self) + time_to_int(duration)
        return Time.int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __str__(self):
        s = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        return s
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return Time.int_to_time(seconds)

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time
start = make_time(9, 40, 0)
Time.print_time(start)
start.print_time()
print()

start = Time.int_to_time(34800)
start.print_time()

end = start.add_time(1, 32, 0)
print_time(end)

print(end.is_after(start))
print(end.__str__())
str(end)
print(end)
print()

time = Time(9, 40, 0)
print(time)
print()

time = Time()
print(time)
print()

time = Time(9)
print(time)
print()

time = Time(9, 45)
print(time)
print()

duration = Time(1, 32)
end = start + duration
print(end)
