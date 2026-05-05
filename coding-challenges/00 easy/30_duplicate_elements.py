"""
Duplicate Elements

Given an array of numbers, return a new array with each element duplicated.

Notes:
- The function should maintain the original order of the numbers.
- Each number should appear twice consecutively.
"""

def double(numbers: list[int]) -> list[int]:
    result = []
    for n in numbers:
        result.append(n)
        result.append(n)
    return result

# Example
print(double([1, 2, 3]))  # [1, 1, 2, 2, 3, 3]
print(double([1,2,3]))    # [1,1,2,2,3,3]
print(double([4]))        # [4,4]
print(double([10,-5,0]))  # [10,10,-5,-5,0,0])