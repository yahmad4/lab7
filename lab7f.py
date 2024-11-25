#!/usr/bin/env python3
#Student Id: yahmad4

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a formatted string for the time object"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation for the object with '.' as separator"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Add two Time objects using the + operator."""
        total_seconds = time_to_sec(self) + time_to_sec(t2)
        return sec_to_time(total_seconds)

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def valid_time(self):
        """Check for the validity of the time object attributes:
           0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60 """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True

    def change_time(self, seconds):
        """Modify the given time object by adding the given seconds,
           handling overflow or underflow correctly using time_to_sec and sec_to_time.
        """
        total_seconds = time_to_sec(self) + seconds
        new_time = sec_to_time(total_seconds)

        # Update the original time object with new values
        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second

    def sum_times(self, other_time):
        """Add another time object to this time object and return the sum."""
        total_seconds = time_to_sec(self) + time_to_sec(other_time)
        return sec_to_time(total_seconds)

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
    t2 = Time(1, 1, 1)

    # Test sum_times
    print("Sum of times (t1.sum_times(t2)):", t1.sum_times(t2))
    print("Sum of times (t2.sum_times(t1)):", t2.sum_times(t1))

    # Test addition using __add__
    t3 = t1 + t2
    print("t1 + t2:", t3)
    print("Type of t1 + t2:", type(t3))
    print("Formatted t1 + t2:", t3)
