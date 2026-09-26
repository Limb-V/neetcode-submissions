from typing import Dict # this adds type hinting for Dict
from collections import Counter
def count_characters(word: str) -> Dict[str, int]:
    count = {}
    count_n = 0
    for ch in word:
        count_n = Counter(word)[ch]
        count[ch] = count_n
    return count




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
