def word_count(book_text):
    count = len(book_text.split())
    return count

def character_count(book_text):
    lowered = book_text.lower()
    letter_counts = {}
    for letter in lowered:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def sort_characters(characters):
    dictionary_list = [
        {
            "char": "", "num": 0
            }
        ]
    banned_list = [
        {
            "char": "", "num": 0
            }
        ]
    for character in characters:
        if character.isalpha() == True:
            dictionary_list.append({"char": character, "num": characters[character]})
        else:
            banned_list.append({"char": character, "num": characters[character]})
    dictionary_list.remove({"char": "", "num": 0})
    return dictionary_list