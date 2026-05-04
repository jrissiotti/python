# Description
# Given a string textand a string prefix, it returns trueif textit starts exactly with prefix, or falseotherwise.
# The comparison is case-sensitive .

def starts_with(text: str, prefix: str) -> bool:
    
    return text[: len(prefix)] == prefix
starts_with("hello python", "hello")