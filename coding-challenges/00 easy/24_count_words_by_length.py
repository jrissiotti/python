"""
Count Words by Length

Given a string of text and an integer n, return how many words 
in the string have exactly n characters.

Notes:
- If the string is empty, return 0.
- Words are separated only by spaces.
- The comparison is exact: the word must have exactly n characters.
- Do not use external libraries.
"""

def count_words_by_length(sentence: str, length: int) -> int:
    return sum(1 for word in sentence.split() if len(word) == length)

# Examples
print(count_words_by_length("hola mundo foo", 4))      # 1
print(count_words_by_length("el gato y el perro", 2))  # 2
print(count_words_by_length("uno dos tres", 3))        # 2
print(count_words_by_length("", 3))                    # 0