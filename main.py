import sys
from stats import count_words, count_characters, sorted_characters

def get_book_text(path) -> str:
    with open(path, "r") as file:
        file_contents: str = file.read()
    return file_contents

def print_report(path: str, num_words: int, sorted_chars: list) -> None:
    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {path}...")
    print("-" * 11 + " Word Count " + "-" * 10)
    print(f"Found {num_words} total words")
    print("-" * 9 + " Character Count " + "-" * 7)
    for char_count in sorted_chars:
        print(f"{char_count['char']}: {char_count['num']}")
    print("=" * 13 + " END " + "=" * 15)

def main() -> None:
    # path = os.path.join("books", "frankenstein.txt")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_contents: str = get_book_text(path)
    num_words: int = count_words(book_contents)
    num_characters: dict = count_characters(book_contents)
    sorted_chars: list = sorted_characters(num_characters)
    print_report(path, num_words, sorted_chars)

if __name__ == "__main__":
    main()
