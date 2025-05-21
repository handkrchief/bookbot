# Given a filepath, reads the content of the file and returns the contents as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

# Given a string, splits the text and counts the number of entries in the list (word count)
def count_words(text):
    split_text = text.split()
    return len(split_text)

def main():
   file_contents = get_book_text("/home/ethan/workspace/bootDev/bookbot/books/frankenstein.txt")
   num_words = count_words(file_contents)
   print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
