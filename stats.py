from typing import List
from collections import defaultdict

def count_words(text: str) -> int:
    words: list = text.split()
    num_words: int = len(words)
    return num_words

def count_characters(text: str) -> defaultdict:
    char_count: defaultdict = defaultdict(int)
    for char in text:
        char_count[char.lower()] += 1
    reg_dict = dict(char_count)
    return reg_dict

def sort_on(items: dict) -> int:
    return items["num"]

def sorted_characters(char_count: dict) -> List[dict]:
    sorted_list: List[dict] = []
    for char, count in char_count.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list