"""
Both area True
Given two boolean values, it returns True only if both are True
"""

def both_true(first_value: bool, second_value: bool) -> bool:
    return first_value and second_value

# Examples
print(f"True and True: {both_true(True, True)}")     #True
print(f"True and False: {both_true(True, False)}")   #False
print(f"False and False: {both_true(False, False)}") #False
print(f"False and True: {both_true(False, True)}")   #False