from stats import word_count, character_count, sort_characters

# A function that takes a text file and makes the content readable
def get_book_text(f):
    with open(f) as f:
        file_contents = f.read()
    return file_contents

# Variable for the content of Frankenstein
book_text = get_book_text("books/frankenstein.txt")

# Variable that holds the value of the word_count function imported from stats.py
words = word_count(book_text)

# Variable that holds the value of the character_count function imported from stats.py
characters = character_count(book_text)

# A helper function to assist with sorting
def sort_on(items):
    return items["num"]

# Variable holding a sorted list of dictionaries containing the number of each character
sorted_char = sort_characters(characters)

# Method to sort characters from largest to smallest
sorted_char.sort(reverse=True, key=sort_on)

# Variable to hold the length of sorted_char list
length_sorted_char = len(sorted_char)

# Prints the results of bookbot in an easy to read format
print("============ BOOKBOT ============\n", 
"Analyzing book found at books/frankenstein.txt...\n", 
"----------- Word Count ----------\n",
# Lists total number of words in book
f"Found {words} total words\n", 
"--------- Character Count -------\n")
# For loop to iterate over list of dictionaries to print each in clean format
for i in range(length_sorted_char): 
    print(f"{sorted_char[i]["char"]}: {sorted_char[i]["num"]}")
print("============= END ==============")