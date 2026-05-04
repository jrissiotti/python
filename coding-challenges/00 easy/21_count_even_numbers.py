"""
Count Even Numbers

Given an array of integers, return the count of even numbers it contains.

Notes:
- A number is even if it is divisible by 2 with no remainder.
- If the array is empty, return 0.
- Consider negative numbers as well.
- Do not use external libraries.
"""

def count_even_numbers(numbers: list[int]) -> int:
    return sum (1 for element in numbers if element % 2 == 0)

# Examples
print(count_even_numbers([1, 2, 3, 4, 5, 6])) # 3
print(count_even_numbers([1, 3, 5]))          # 0
print(count_even_numbers([]))                 # 0
