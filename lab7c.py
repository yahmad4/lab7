#!/usr/bin/env python3
# Student ID: yahmad4

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def valid_time(t):
    """Check for the validity of the time object attributes:
       0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True

def sum_times(t1, t2):
    """Add two time objects and return the sum using time_to_sec and sec_to_time."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Modify the given time object by adding the given seconds,
       handling overflow or underflow correctly using time_to_sec and sec_to_time.
    """
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)

    # Update the original time object with new values
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second

def time_to_sec(time):
    """Convert a Time object to total seconds."""
    return time.hour * 3600 + time.minute * 60 + time.second

def sec_to_time(seconds):
    """Convert total seconds to a Time object."""
    hour = seconds // 3600 % 24
    minute = (seconds % 3600) // 60
    second = seconds % 60
    return Time(hour, minute, second)

# Example usage for testing
if __name__ == "__main__":
    t1 = Time(9, 50, 0)
    print("Initial time:", format_time(t1))

    # Test sum_times
    t2 = Time(1, 20, 0)
    tsum = sum_times(t1, t2)
    print("Sum of times:", format_time(tsum))

    # Test change_time with positive seconds
    change_time(t1, 1800)
    print("Time after adding 1800 seconds:", format_time(t1))

    # Test change_time with negative seconds
    change_time(t1, -1800)
    print("Time after subtracting 1800 seconds:", format_time(t1))

