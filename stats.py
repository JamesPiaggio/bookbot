# Function that gives a total word count from a book
def word_count(book_text):
    # Method splits each word into a separate string then gives length
    count = len(book_text.split())
    return count

# Function that gives a total character count of a book and records each time character appears
def character_count(book_text):
    # Puts all text in lowercase
    lowered = book_text.lower()
    # Declared empty dictionary
    letter_counts = {}
    # For loop to go through each letter in text
    for letter in lowered:
        # If letter is already in dictionary, add 1
        if letter in letter_counts:
            letter_counts[letter] += 1
        # Else create entry and set to 1
        else:
            letter_counts[letter] = 1
    return letter_counts

# Function that sorts characters in a list of dictionaries with keys and removes "banned" characters
def sort_characters(characters):
    # Declared empty list of dictionaries for characters
    dictionary_list = [
        {
            "char": "", "num": 0
            }
        ]
    # Declared empty list of dictionaries for "banned" characters
    banned_list = [
        {
            "char": "", "num": 0
            }
        ]
    # For loop to go through each dictionary entry in character list
    for character in characters:
        # If character is part of the alphabet, add to dictionary_list
        if character.isalpha() == True:
            dictionary_list.append({"char": character, "num": characters[character]})
        # Else add to banned_list
        else:
            banned_list.append({"char": character, "num": characters[character]})
    # Removes empty entries in dictionary_list
    dictionary_list.remove({"char": "", "num": 0})
    return dictionary_list