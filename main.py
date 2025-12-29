from stats import word_count, character_count, sort_characters

def get_book_text(f):
    with open(f) as f:
        file_contents = f.read()
    return file_contents

book_text = get_book_text("books/frankenstein.txt")

words = word_count(book_text)
characters = character_count(book_text)

def sort_on(items):
    return items["num"]

sorted_char = sort_characters(characters)
sorted_char.sort(reverse=True, key=sort_on)

length_sorted_char = len(sorted_char)

print("============ BOOKBOT ============\n", 
"Analyzing book found at books/frankenstein.txt...\n", 
"----------- Word Count ----------\n", 
f"Found {words} total words\n", 
"--------- Character Count -------\n")
for i in range(length_sorted_char):
    print(f"{sorted_char[i]["char"]}: {sorted_char[i]["num"]}")
print("============= END ==============")