"""
Convert to Uppercase

Given a string, return it converted entirely to uppercase.

Notes:
- The function should handle strings with mixed casing.
- An empty string should return an empty string.
"""

def to_upper_case(text: str) -> str:
    return text.upper()

# Examples
print(to_upper_case("hola"))        # "HOLA"
print(to_upper_case("TypeScript"))  # "TYPESCRIPT"
print(to_upper_case(""))            # ""