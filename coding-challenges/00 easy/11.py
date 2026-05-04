"""
Count Consonants

Write a function `count_consonants` that receives a string and returns the 
number of consonants it contains.

Consonants are all the letters of the alphabet except for vowels (a, e, i, o, u). 
Consider both uppercase and lowercase. Ignore any character that is not a letter.

Restrictions:
- The string can contain any character (numbers, spaces, punctuation marks).
- Only consonant letters count (a-z, A-Z excluding vowels).
- Do not use external libraries.
"""

def count_consonants(text: str) -> int:
    consonants = []
    vowels = ["a", "e", "i", "o", "u"]
    for element in text.lower():
        if element in vowels or element == " ":
            continue
        elif not element.isalpha():
            continue
        consonants.append(element)
    return len(consonants)

# Examples
print(count_consonants("Hola Mundo"))    # 5
print(count_consonants("aeiou"))         # 0
print(count_consonants("TypeScript"))    # 8
print(count_consonants(""))              # 0
print(count_consonants("123 abc!"))      # 2