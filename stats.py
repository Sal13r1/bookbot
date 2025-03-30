def count_words(text):
    num_words = 0
    words = text.split()

    for word in words:
        num_words += 1

def count_letters(text):
    letter_dict = {}
    words = text.lower()
    for word in words:
        for letter in word:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

    for letter in letter_dict:
        print(f"'{letter}': {letter_dict[letter]}")
    return letter_dict