"""
Count Unique Words

Given a text string, return the number of unique words it contains. 
Words are separated by spaces, and the comparison is case-insensitive.

Notes:
- Ignore case (e.g., 'Hola' and 'hola' are the same).
- An empty string returns 0.
"""

def count_unique_words(text: str) -> int:
    return len(set(text.lower().split()))

# Examples
print(count_unique_words("hola mundo hola"))          # 2
print(count_unique_words("TypeScript es genial es"))  # 3
print(count_unique_words("uno"))                      # 1
print(count_unique_words(""))                         # 0