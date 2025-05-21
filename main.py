from stats import count_words
from stats import count_characters
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
   if len(sys.argv) == 1:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
   file_contents = get_book_text(sys.argv[1])

   num_words = count_words(file_contents)
   print(f"Found {num_words} total words")

   num_chars = count_characters(file_contents)
   sorted_chars = sort_dict(num_chars)
   for small_dictionary in sorted_chars:
      if small_dictionary["char"].isalpha():
        print(f"{small_dictionary['char']}: {small_dictionary['num']}")

   

if __name__ == "__main__":
    main()
