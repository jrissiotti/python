"""
Number Clamp

Given a number and a range [min, max], return the number limited within that range.If the number is less than min,
return min.If the number is greater than max, return max.If the number is within the range, return the number as is.

Notes:
- You can assume that min <= max is always true.
- The range is inclusive at both ends.
"""

def clamp_number(num: int, min_val: int, max_val: int) -> int:
    
    if num < min_val:
        return print(min_val)
    elif num > max_val:
        return print(max_val)
    else:
        return print(num)

clamp_number(5, 1, 10)  # 5  → within range
clamp_number(0, 1, 10)  # 1  → less than min, returns min
clamp_number(15, 1, 10) # 10 → greater than max, returns max
clamp_number(1, 1, 10)  # 1  → equal to lower limit, it is valid