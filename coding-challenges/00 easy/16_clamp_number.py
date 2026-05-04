"""
Number Clamp

Given a number and a range [min, max], return the number limited within that range.If the number is less than min,
return min.If the number is greater than max, return max.If the number is within the range, return the number as is.

Notes:
- You can assume that min <= max is always true.
- The range is inclusive at both ends.
"""

def clamp_number(num: int, min_val: int, max_val: int) -> int:
    return print (max(min_val, min(num, max_val)))

# Examples
clamp_number(5, 1, 10)  # 5
clamp_number(0, 1, 10)  # 1
clamp_number(15, 1, 10) # 10
clamp_number(1, 1, 10)  # 1