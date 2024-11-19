def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def main():
    # Change later to utilize user input
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    
    # Print statement for error checking
    print(f"Found {word_count} words in this document.")

main()