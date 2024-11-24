#!/usr/bin/env python3
# Student ID: yahmad4

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string."""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the normalized sum."""
    # Create a new Time object to store the sum
    sum = Time()
    sum.second = t1.second + t2.second
    sum.minute = t1.minute + t2.minute + sum.second // 60
    sum.hour = t1.hour + t2.hour + sum.minute // 60

    # Normalize values
    sum.second %= 60
    sum.minute %= 60
    sum.hour %= 24

    return sum

def change_time(time, seconds):
    """Modify the time object by adding/subtracting seconds."""
    time.second += seconds

    # Normalize seconds and minutes
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.second < 0:
        time.second += 60
        time.minute -= 1

    # Normalize minutes and hours
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    # Normalize hours within the range 0-23
    time.hour %= 24

    return None

def valid_time(t):
    """Check for the validity of the time object attributes:
        0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60
    """
    if t.hour < 0 or t.hour >= 24:
        return False
    if t.minute < 0 or t.minute >= 60:
        return False
    if t.second < 0 or t.second >= 60:
        return False
    return True

# Example Usage
if __name__ == "__main__":
    t1 = Time(10, 45, 50)
    t2 = Time(2, 20, 15)
    t3 = sum_times(t1, t2)

    print("Time 1:", format_time(t1))
    print("Time 2:", format_time(t2))
    print("Sum of Times:", format_time(t3))
    print("Is Time 1 valid?", valid_time(t1))
    print("Is Time 3 valid?", valid_time(t3))

    # Testing change_time
    seconds = 1800
    change_time(t1, seconds)
    print("Time 1 after adding 1800 seconds:", format_time(t1))

    seconds = -1800
    change_time(t1, seconds)
    print("Time 1 after subtracting 1800 seconds:", format_time(t1))
