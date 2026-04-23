# Given two boolean values, it returns True only if both are True

def at_least_one_true(first_value: bool, second_value: bool) -> bool:
    
    if first_value and second_value:
        return True
    else:
        return False
at_least_one_true(True, False)