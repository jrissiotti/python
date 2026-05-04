"""
Is Divisible?

Given two numbers 'n' and 'divisor', return true if 'n' 
is divisible by 'divisor' (with no remainder).

Notes:
- Return True if the remainder is 0.
- Otherwise, return False.
- Do not use external libraries.
"""

def is_divisible(value: int, divisor: int) -> bool:
    return value % divisor == 0 

# Examples
print(is_divisible(10, 2)) # True
print(is_divisible(7, 2))  # False
print(is_divisible(9, 3))  # True