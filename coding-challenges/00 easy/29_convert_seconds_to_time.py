"""
Convert Seconds to Time

Given an integer number of seconds (greater than or equal to 0), 
return a string in the format "HH:MM:SS" representing hours, 
minutes, and seconds.

Restrictions:
- seconds >= 0
- Each component must have exactly 2 digits (with a leading zero if necessary).
"""

def seconds_to_time(seconds: int) -> str:
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"
# Examples
print(seconds_to_time(0))      # "00:00:00"
print(seconds_to_time(61))     # "00:01:01"
print(seconds_to_time(3661))   # "01:01:01"
print(seconds_to_time(86399))  # "23:59:59"