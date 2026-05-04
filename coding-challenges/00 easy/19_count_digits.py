"""
Count Digits

Given an integer, return the number of digits it contains.

Note: The negative sign does not count as a digit. 
The number 0 has 1 digit.

Restrictions:
- The argument will always be an integer.
- Negative numbers should only count their digits (excluding the sign).
"""

def count_digits(n: int) -> int:
    return len(str(abs(n)))
        
# Examples
print(count_digits(12345)) # 5
print(count_digits(0))     # 1
print(count_digits(-42))   # 2
print(count_digits(7))     # 1