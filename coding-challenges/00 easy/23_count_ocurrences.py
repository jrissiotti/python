"""
Count Occurrences in Array

Given an array of numbers and a target value, return how many 
times that value appears in the array.

Notes:
- If the array is empty, return 0.
- If the target value is not in the array, return 0.
- Do not use external libraries.
"""

def count_occurrences(numbers: list[int], target: int) -> int:
    return sum(1 for element in numbers if element == target)

# Examples
print(count_occurrences([1, 2, 3, 2, 2, 4], 2)) # 3
print(count_occurrences([5, 5, 5, 5], 5))       # 4
print(count_occurrences([1, 2, 3], 7))          # 0
print(count_occurrences([], 1))                 # 0