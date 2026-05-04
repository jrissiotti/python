"""
Count Unique Characters

Given a string, return the number of distinct characters it contains (without 
counting repetitions). The comparison is case-sensitive, meaning 'A' and 'a' 
are considered different characters.

Notes:
- An empty string returns 0.
- Spaces also count as characters.
- Do not use external libraries.
"""

def count_unique_chars(text: str) -> int:


    unique_chars = []

    for element in text:
        if element in unique_chars:
            continue
        unique_chars.append(element)
    return len(unique_chars)

# Test cases
print(count_unique_chars("hello"))    # 4  (h, e, l, o)
print(count_unique_chars("aabbcc"))   # 3  (a, b, c)
print(count_unique_chars("abcABC"))   # 6  (a, b, c, A, B, C)
print(count_unique_chars(""))         # 0
print(count_unique_chars("a A b B")) # 5  (including space)