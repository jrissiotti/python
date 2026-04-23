# Given two booleans, it returns True if at least one of them is True

def at_least_one_true(first_value: bool, second_value: bool) -> bool:
    
    if first_value or second_value:
        return True
    else:
        return False
at_least_one_true(True, False)