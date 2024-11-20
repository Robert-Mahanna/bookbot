# Function to open and read a file from a directory
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
# Function to count the number of words in a string; split by white space
def get_word_count(text):
    words = text.split()
    return len(words)

# Function to count the number of times each character appears in a string
def get_character_count(text):
    character_counter = {}
    for character in text:
        lowered = character.lower()
        if lowered in character_counter:
            character_counter[lowered] += 1
        else:
            character_counter[lowered] = 1
    return character_counter


def main():
    # TODO: Change book_path to utilize user input
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    character_count = get_character_count(text)
    word_count = get_word_count(text)
    
    # Print statements for error checking
    # print(text)
    # print(f"Found {word_count} words in this document.")
    print(character_count)

main()