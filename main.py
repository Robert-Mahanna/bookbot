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

# Function used to know how to sort the new list
def sort_on(dictionary):
    return dictionary["number"]

# Funtion to make a list of alphabetical characters in a dictionary
def make_alpha_list(dictionary):
    new_list = []
    key_value_dictionary = {}
    for key in dictionary:
        if key.isalpha() == True:
            key_value_dictionary = {"character": key, "number": dictionary[key]}
            new_list.append(key_value_dictionary)
    return sorted(new_list, key=sort_on, reverse=True)

# Function to run a report on word and character count of a document
def run_report(path, count, list):
    print(f"--- Begin report of {path} ---\n")
    print(f"{count} words found in {path}.\n")
    for dictionary in list:
        character_value = ""
        number_value =""
        for key, value in dictionary.items():
            if character_value == "":
                character_value = value
            else:
                number_value = value
        print(f"The '{character_value}' character was found {number_value} times.")
    print("\n--- End report ---")



def main():
    # TODO: Change book_path to utilize user input
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    character_list = make_alpha_list(character_count)
    run_report(book_path, word_count, character_list)
    
    # Print statements for error checking
    # print(text)
    # print(f"Found {word_count} words in this document.")
    # print(character_count)
    # print(character_list)

main()