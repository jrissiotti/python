"""
Does it contain the character?
Returns True if the string contains the given character, False otherwise
"""
def contains_char(text: str, char: str) -> bool:  
    return char in text

# Examples
print(f"Is 'a' in 'banana'?: {contains_char('banana', 'a')}")   # True
print(f"Is 'z' in 'apple'?: {contains_char('apple', 'z')}")     # False
print(f"Is 'x' in 'box'?: {contains_char('box', 'x')}")         # True