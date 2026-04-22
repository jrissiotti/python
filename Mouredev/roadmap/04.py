#04 character strings

"""
Operations
"""

s1 = "Hello"
s2 = "Python"

# concatenation
print(s1 + " " + s2 + "!")

# repetition
print(s1 * 5)

# indexing
print(s1[0] + s1[2] + s2[4])

# length
print(len(s2))

# slicing
print(s2[2:4])
print(s2[2:])
print(s2[:2])

# search
print("He" in s1)
print("a" in s1)

# replacement
print(s1.replace ("o", "u"))

# division
print(s2.split("t"))

# uppercase and lowercase
print(s1.upper())
print(s2.lower())
print("jorge alejandro rissiotti".title())
print("jorge alejandro rissiotti".capitalize())

# removing leading and trailing space
print ("    jorge rissiotti    ".strip())

# search at the beginning and end
print(s1.startswith("He"))
print(s1.endswith("la"))
print(s2.startswith("X"))
print(s2.endswith("on"))

s3 = "Jorge Alejandro Rissiotti @jrissiotti"

# position search
print(s3.find("j"))
print(s3.lower().find("j"))

# search for occurrences
print(s3.lower().count("rissiotti"))

# formatting
print("Greet: {}, language: {}!".format(s1, s2))

#interpolation -> f-string
print(f"Greet: {s1}, language: {s2}!")

# transformation into a character list
print(list(s3))

# list to string transformation
l1 = [s1, s2, "!"]
print("-". join(l1))
print(type("-". join(l1)))

# numerical transformations
s4 = "12345"
s4 = int(s4)
print(s4)

s5 = "12345.123"
s5 = float(s5)
print(s5)

# various checks
s4 = "12345"
print(s1.isalnum())
print(s2.isalnum())
print(s4.isalpha())
print(s4.isnumeric())

"""
Extra

english: Create a program that analyzes two different words and performs checks to determine if they are:
        - Palindromes
        - Anagrams
        - Isograms

spanish: Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
        - Palíndromos
        - Anagramas
        - Isogramas
"""

