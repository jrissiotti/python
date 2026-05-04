
"""
Starts with Prefix?

Given a string 'text' and a string 'prefix', return true if 'text' 
starts exactly with 'prefix', or false otherwise.

Notes:
- The comparison is case-sensitive.
- An empty string as a prefix should return True.
"""

def starts_with(text: str, prefix: str) -> bool:
    return text[: len(prefix)] == prefix

# Examples
print(starts_with("hola mundo", "hola"))    # True
print(starts_with("hola mundo", "Hola"))    # False
print(starts_with("TypeScript", "Type"))    # True
print(starts_with("TypeScript", "script"))  # False
print(starts_with("", ""))                  # True
print(starts_with("abc", ""))               # True