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
    return len(set(text))

# Examples
print(count_unique_chars("hello"))    # 4
print(count_unique_chars("aabbcc"))   # 3
print(count_unique_chars("abcABC"))   # 6
print(count_unique_chars(""))         # 0
print(count_unique_chars("a A b B"))  # 5