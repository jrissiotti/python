"""
Value and Reference
"""

# Data types by value (Immutables)

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
# my_int_a = 30
print(my_int_a)  # Output: 10
print(my_int_b)  # Output: 20

# Data types by reference (Mutables)

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)  # Output: [10, 20, 30]
print(my_list_b)  # Output: [10, 20, 30]

# Functions with data by value

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)  # Local change: 20

my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)  # Original remains: 10

# Functions with data by reference

def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)   # Both show updated list
    print(my_list_d)

my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)  # Original is modified: [10, 20, 30, 40]

"""
Extra: Swapping Challenges
"""

# By value (The originals don't change)

def swap_value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = swap_value(my_int_d, my_int_e)

print(f"Originals: {my_int_d}, {my_int_e}")
print(f"Swapped: {my_int_f}, {my_int_g}")

# By reference (Reassigning the variable inside doesn't affect the original pointer)

def swap_ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = swap_ref(my_list_e, my_list_f)

print(f"Originals: {my_list_e}, {my_list_f}")
print(f"Swapped: {my_list_g}, {my_list_h}")