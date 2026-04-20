"""
ENGLISH: Create a program that transforms
         a decimal number to binary.
         
SPANISH: Crea un programa que transforme un
         numero decimal a binario.
"""

def decimal_to_binary(decimal):
    my_binary = ""

    while decimal > 0:
        my_binary = str(decimal % 2) + my_binary
        decimal //= 2

    return my_binary

print(decimal_to_binary(11))