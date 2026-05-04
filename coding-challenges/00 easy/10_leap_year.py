"""
Leap Year

A year is a leap year if it meets any of these conditions:
- It is divisible by 400, OR
- It is divisible by 4 but NOT by 100.

Write a function that receives an integer 'year' and returns True 
if it is a leap year, or False otherwise.
"""

def is_leap_year(year: int) -> bool:
    return True if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else False

# Examples
print(is_leap_year(2000)) # True  (divisible by 400)
print(is_leap_year(1900)) # False (divisible by 100 but not 400)
print(is_leap_year(2024)) # True  (divisible by 4 and not 100)
print(is_leap_year(1999)) # False (not divisible by 4)