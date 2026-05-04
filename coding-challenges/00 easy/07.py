"""
Calculate the average of a list

Write a function that receives a list of numbers and returns their average (arithmetic mean).
The average is calculated by adding all the elements and dividing by the number of elements.
"""
def average(numbers: list[float]) -> float:
    
    if numbers:
        addition = 0
        for element in numbers:
            addition += element
        return print(addition / len(numbers))
    return print(0.0)

average([1, 2, 3, 4, 5])
average([10, 20, 30])
average([7])
average([])