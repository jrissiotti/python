"""
Count Vowels

Given a string, return the number of vowels it contains (a, e, i, o, u).
The count must be case-insensitive, meaning both 'A' and 'a' count as vowels.

Notes:
- Only vowels from the English alphabet are considered: a, e, i, o, u.
- If the string is empty, return 0.
"""

def count_vowels(text: str) -> int:
    return sum(1 for element in text.lower() if element in "aeiou")

# Examples
print(count_vowels("hola"))     # 2
print(count_vowels("AEIOU"))    # 5
print(count_vowels("python"))   # 1
print(count_vowels(""))         # 0
print(count_vowels("bcdfgh"))   # 0