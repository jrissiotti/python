"""
Count Negative Elements

Given an array of numbers, return the count of elements that are 
strictly less than 0.

Notes:
- Zero is NOT considered negative.
- If the array is empty, return 0.
- Do not use external libraries.
"""

def count_negatives(numbers: list[int]) -> int:
    return sum(1 for n in numbers if n < 0)

# Examples
print(count_negatives([-1, 2, -3, 4, 0])) # 2
print(count_negatives([1, 2, 3]))         # 0
print(count_negatives([-5, -10, -1]))     # 3
print(count_negatives([]))                # 0