# Given two booleans, it returns True if at least one of them is True

def at_least_one_true(first_value: bool, second_value: bool) -> bool:
    
    return first_value or second_value

print(f"True or True: {at_least_one_true(True, True)}")     #True
print(f"True or False: {at_least_one_true(True, False)}")   #True
print(f"False or False: {at_least_one_true(False, False)}") #False
print(f"False or True: {at_least_one_true(False, True)}")   #True