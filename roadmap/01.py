# operators and control structure

"""
Operators
"""

# Aritmetic operators
print(f"Addition: 4 + 3 = {4 + 3}")
print(f"Substraction: 4 - 3 = {4 - 3}")
print(f"Multiplication: 4 * 3 = {4 * 3}")
print(f"Division: 4 / 3 = {4 / 3}")
print(f"Integer division: 4 // 3 = {4 // 3}")
print(f"Modulus: 4 % 3 = {4 % 3}")
print(f"Exponent: 4 ** 3 = {4 ** 3}")

# Comparison operators
print(f"Equality: 6 == 4: {6 == 4}")
print(f"Inequality: 6 != 4: {6 != 4}")
print(f"Lesser: 6 < 4: {6 < 4}")
print(f"Greater: 6 > 4: {6 > 4}")
print(f"Lesser than or equal to: 6 <= 4: {6 <= 4}")
print(f"Greater than or equal to: 6 >= 4: {6 >= 4}")

# Logic operators
print(f"AND: 8 + 3 == 11 and 9 - 3 == 6 is {8 + 3 == 11 and 9 - 3 == 6}")
print(f"OR: 8 + 3 == 12 or 9 - 3 == 6 is {8 + 3 == 12 or 9 - 3 == 6}")
print(f"NOT: not 8 + 3 == 11 is {not 8 + 3 == 11}")

# Assignment operators -> They perform the operation and then assign it.
my_number = 14
print(my_number)
my_number += 14
print(my_number)
my_number -= 14
print(my_number)
my_number *= 14
print(my_number)
my_number /= 14
print(my_number)
my_number //= 14
print(my_number)
my_number %= 14
print(my_number)
my_number **= 14
print(my_number)

# Identity operators
my_new_number = 12
print(f"my_number is my_new_number is: {my_number is my_new_number}")

# Membership operators
print(f" 'a' in 'jorge' = {'a' in 'jorge'}")

# Bit operators
a = 10 #1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") #0010 =  2
print(f"OR: 10 | 3 = {10 | 3}") #1011 = 11
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #1001 = 9
print(f"NOT: ~10 = {~10}") 
print(f"Right shift: 10 >> 2 = {10 >> 2}") #1010 -> 0010 = 2
print(f"Left shift: 10 << 2 = {10 << 2}") #1010 <- 101000 = 40




# Less common operators

# Walrus operator (:=)
# Assigns a value inside an expression
if (n := 10) > 5:
    print(f"Walrus operator: n is {n}")

# Ternary operator (inline if-else)
x = 7
result = "greater than 5" if x > 5 else "less or equal to 5"
print(f"Ternary operator: x is {result}")

# String and list operations (important in practice)

# Concatenation
print(f"Concatenation: 'Hello' + ' World' = {'Hello' + ' World'}")

# Repetition
print(f"Repetition: 'Hi' * 3 = {'Hi' * 3}")

# Membership in collections (more examples)
my_list = [1, 2, 3, 4]
print(f"2 in list: {2 in my_list}")
print(f"5 not in list: {5 not in my_list}")

# Identity deeper example
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"a is b: {a is b}")   # True (same object)
print(f"a is c: {a is c}")   # False (different objects)
print(f"a == c: {a == c}")   # True (same content)

"""
Control structures
"""

# Conditionals

my_string = "Jorge"
if my_string == "Jorge":
    print("my_string is 'Jorge'")
elif my_string == "Rissiotti":
    print("my_string is 'Rissiotti'")
else:
    print("my_string is neither 'Jorge' nor 'Rissiotti'")

# Iteratives
for i in range(9):
    print(i)

i=0
while i <= 10:
    print(i)
    i += 2

# Exception handling
try:
    print(10/0)
except:
    print("An error has occurred")
finally:
    print("Error handling has ended")

"""
EXTRA:
ENGLISH: Create a program that prints to the console all the numbers between 10 and 55 (inclusive),
         even numbers, and that are neither 16 nor multiples of 3.

SPANISH: Crea un programa que imprima por consola todos los números comprendidos
         entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
print("*" *5 + " EXTRA EXERCISE " + "*" *5 )
for number in range(10,56, 2):
    if number != 16 and number % 3 != 0:
        print(number)