"""
Calculate the average of a list

Write a function that receives a list of numbers and returns their average (arithmetic mean).
The average is calculated by adding all the elements and dividing by the number of elements.
"""

def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0

# Examples
print(average([1, 2, 3, 4, 5])) # 3.0
print(average([10, 20, 30]))    # 20.0
print(average([7]))             # 7.0
print(average([]))              # 0.0