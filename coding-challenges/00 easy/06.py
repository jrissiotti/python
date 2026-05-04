""" 
Flatten a level

Given a list that can contain single items or sublists, this will return a new list with a single level of flattening.
Unlike full flattening, here only the top-level sublists are removed. If a sublist contains another nested list, that
nested list is retained as an item.
"""

def flatten_one_level(array: list) -> list:

    new_array = []

    for element in array:

        if isinstance(element, list):
            new_array.extend(element)
        else:
            new_array.append(element)
    return print(new_array)

flatten_one_level([1, [2, 3], [4, 5]])
flatten_one_level([1, [2, [3, 4]], 5])
flatten_one_level([[1, 2], [3, 4]])
flatten_one_level([])
flatten_one_level([1, 2, 3])