"""
Convert to Lowercase

Given a string, return it converted entirely to lowercase.

Notes:
- The function should handle strings with mixed casing.
- An empty string should return an empty string.
"""

def to_lower_case(text: str) -> str:
    return text.lower()

# Examples
print(to_lower_case("HOLA"))        # "hola"
print(to_lower_case("TypeScript"))  # "typescript"
print(to_lower_case(""))            # ""