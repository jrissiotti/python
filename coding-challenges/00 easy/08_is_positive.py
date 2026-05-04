"""
Is it Positive?

Returns true if the number is greater than 0, false otherwise.

Notes:
- Zero is not considered a positive number in this specific challenge.
- The function should handle both integers and floats.
"""

def is_positive(value: float) -> bool:
    return True if value > 0 else False

# Examples
print(is_positive(5))  # True
print(is_positive(-3)) # False
print(is_positive(0))  # False