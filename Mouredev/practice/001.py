"""
ENGLISH: Create an exercise that checks
         whether a number is even or odd.

SPANISH: Crea un ejercicio que compruebe
         si un numero es par o impar
"""

def is_even_or_odd():
    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            return f"{number} is even"
        else:
            return f"{number} is odd"
    except ValueError:
        return "Fatal error, enter an integer number"
print(is_even_or_odd())