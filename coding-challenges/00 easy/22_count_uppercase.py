"""
Count Uppercase Letters

Given a string, return the count of uppercase letters it contains.

Notes:
- Only uppercase alphabet letters (A-Z) should be counted.
- Numbers, symbols, and spaces do not count.
- If the string is empty, return 0.
"""

def count_uppercase(text: str) -> int:
    return sum(1 for char in text if char.isupper())

# Examples
print(count_uppercase("Hola Mundo"))        # 2
print(count_uppercase("TYPESCRIPT"))        # 10
print(count_uppercase("sin mayusculas"))    # 0
print(count_uppercase(""))                  # 0