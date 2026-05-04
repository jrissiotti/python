"""
capitalize first letter

Given a text string, return the same string with the first letter capitalized and the rest unmodified.

Notes
- If the string is empty, return an empty string.
- Do not modify the other characters in the string.
- The first character may already be in uppercase; in that case, return it as is.
"""

def capitalize_first_letter(text: str) -> str:
    return text[0].upper() + text[1:] if text else ""

# Examples
print(f"'{capitalize_first_letter('hello')}'")      # 'Hello'
print(f"'{capitalize_first_letter('world')}'")      # 'World'
print(f"'{capitalize_first_letter('TypeScript')}'") # 'TypeScript'
print(f"'{capitalize_first_letter('')}'")           # ''