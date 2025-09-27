def count_words(text: str) -> int:
    words: list = text.split()
    num_words: int = len(words)
    return num_words