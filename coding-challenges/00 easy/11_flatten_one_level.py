""" 
Flatten a level

Given a list that can contain single items or sublists, this will return a new list with a single level of flattening.
Unlike full flattening, here only the top-level sublists are removed. If a sublist contains another nested list, that
nested list is retained as an item.
"""

def flatten_one_level(array: list) -> list:
    """
    Returns a new list with a single level of nesting removed.
    """
    return [item for sublist in array for item in (sublist if isinstance(sublist, list) else [sublist])]

# Examples
print(flatten_one_level([1, [2, 3], [4, 5]]))     # [1, 2, 3, 4, 5]
print(flatten_one_level([1, [2, [3, 4]], 5]))     # [1, 2, [3, 4], 5]
print(flatten_one_level([[1, 2], [3, 4]]))        # [1, 2, 3, 4]
print(flatten_one_level([]))                      # []
print(flatten_one_level([1, 2, 3]))               # [1, 2, 3]