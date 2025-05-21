from stats import count_words
from stats import count_characters

# Given a filepath, reads the content of the file and returns the contents as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
   file_contents = get_book_text("/home/ethan/workspace/bootDev/bookbot/books/frankenstein.txt")
   num_words = count_words(file_contents)
   print(f"{num_words} words found in the document")
   num_chars = count_characters(file_contents)
   print(num_chars)
   

if __name__ == "__main__":
    main()
