from stats import *
import sys
if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

book_path = sys.argv[1]

print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {words_count(book_path)} total words\n--------- Character Count -------")
print_char_stats(book_path)
print("============= END ===============")