# Does it contain the character?
# Returns True if the string contains the given character, False otherwise

def contains_char(text: str, char: str) -> bool:
    if char in text:
        return True
    else:
        return False
contains_char("hola", "o")