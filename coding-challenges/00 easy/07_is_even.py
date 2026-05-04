"""
Is it Even?

Create a function that receives a number and returns true 
if it is even, and false if it is odd.

Notes:
- An even number is any integer that is exactly divisible by 2.
- Zero is considered an even number.
"""

def is_even(number: int) -> bool:
    return number % 2 == 0

# Examples
print(is_even(4)) # True
print(is_even(7)) # False