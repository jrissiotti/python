"""
capitalize first letter

Given a text string, return the same string with the first letter capitalized and the rest unmodified.

Notes
- If the string is empty, return an empty string.
- Do not modify the other characters in the string.
- The first character may already be in uppercase; in that case, return it as is.
"""

def capitalize_first_letter(text: str) -> str:

    if text == "":
        return print("")
    return print(text[0].upper() + text[1:])

capitalize_first_letter("hola")
capitalize_first_letter("mundo")
capitalize_first_letter("TypeScript")
capitalize_first_letter("")