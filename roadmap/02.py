# 02 functions and scope

"""
User-defined functions
"""

# Simple
def greet ():
    print("Hello Python!")

greet()

# With return
def return_greet():
    return "Hi Python!"

print(return_greet())

# With argument
def arg_greet(name):
    print(f"Hola {name}")

arg_greet("Jorge")

# With arguments
def args_greet(greet, name):
    print(f"{greet} {name}")

args_greet("Hi", "Jorge")

# With default argument
def default_arg_greet(name = "Python"):
    print(f"Hola {name}")

default_arg_greet("Jorge")
default_arg_greet()

# With arguments and return
def return_args_greet(greet, name):
    return f"{greet} {name}"

print(return_args_greet("Hi", "Jorge"))

# With return of multiple values
def multiple_return_greet():
    return "Hello", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# With a variable number of arguments
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola {name}")

variable_arg_greet("python", "javascript", "typescript")

# With a variable number of arguments with key word
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})")

variable_key_arg_greet(
    language="python",
    name="Jorge",
    apellido="Rissiotti",
    age=19,
    alias="jrissiotti"
)


"""
Functions within functions
"""
def outer_function():
    def inner_function():
        print("Internal function: Hello Pyton")
    inner_function()

outer_function()


"""
Language functions (built-in)
"""
print(len("jrissiotti"))
print(type(19))
print("jrissiotti".upper())


"""
Local and global variables
"""

global_variable = "python"
print(global_variable)

def hello_python():
    # global local_variable 
    local_variable = "Hola"
    print(f"{local_variable} {global_variable}")

hello_python()
# print(local_variable)

"""
Extra:
English: Create a function that takes two string parameters and returns a number.
        - The function prints all the numbers from 1 to 100. Note that:
        - If the number is a multiple of 3, it displays the string from the first parameter.
        - If the number is a multiple of 5, it displays the string from the second parameter.
        - If the number is a multiple of both 3 and 5, it displays the two strings concatenated.
        - The function returns the number of times the number was printed instead of the strings.
Spanish: Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
         - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
         - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
         - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
         - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
         - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
def print_count (string_1, string_2) -> float:
    my_count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(string_1 + string_2)
        elif number % 3 == 0:
            print(string_1)
        elif number % 5 == 0:
            print(string_2)
        else:
            print(number)
            my_count += 1
    return f"Number prints = {my_count}"
print(print_count("Fizz", "Buzz"))