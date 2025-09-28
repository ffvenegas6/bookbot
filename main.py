import os
from stats import count_words, count_characters

def get_book_text(path) -> str:
    with open(path, "r") as file:
        file_contents: str = file.read()
    return file_contents

def main() -> None:
    path = os.path.join("books", "frankenstein.txt")
    book_contents: str = get_book_text(path)
    num_words: int = count_words(book_contents)
    print(f"Found {num_words} total words")
    num_characters = count_characters(book_contents)
    print(num_characters)

if __name__ == "__main__":
    main()
