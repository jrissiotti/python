"""
Common Characters

Given two text strings, return the number of distinct characters that appear 
in both strings. The comparison must be case-insensitive.

Notes:
- Ignore case (e.g., 'A' and 'a' are the same).
- Count each character only once, even if it appears multiple times.
"""

def common_chars(str1: str, str2: str) -> int:
    return len(set(str1.lower()) & set(str2.lower()))

# Examples
print(common_chars("hello", "world"))           # 2
print(common_chars("abc", "ABC"))               # 3
print(common_chars("abcd", "efgh"))             # 0
print(common_chars("", "hello"))                # 0
print(common_chars("typescript", "javascript")) # 6