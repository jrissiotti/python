"""
Is Multiple?

Given two numbers 'n' and 'm', return true if 'n' is a multiple of 'm', 
meaning 'n' is divisible by 'm' with no remainder.

Special Cases:
- If 'm' is 0, return false (division by zero is undefined).
- 0 is a multiple of any number other than zero.
"""

def is_multiple(n: int, m: int) -> bool:
    return False if m == 0 or n % m != 0 else True

# Examples
print(is_multiple(10, 2)) # True  -> 10 / 2 = 5, no remainder
print(is_multiple(9, 3))  # True  -> 9 / 3 = 3, no remainder
print(is_multiple(7, 2))  # False -> 7 / 2 = 3.5, has remainder
print(is_multiple(0, 5))  # True  -> 0 / 5 = 0, no remainder
print(is_multiple(5, 0))  # False -> division by zero