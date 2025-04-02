def count_words(text):
    num_words = 0
    words = text.split()

    for word in words:
        num_words += 1

    return num_words

def count_letters(text):
    letter_dict = {}
    words = text.lower()
    for word in words:
        for letter in word:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def sort_on(dict_item):
    return dict_item['count']

def sort_stats(dictionary):
    sorted_list = []

    for char, entry in dictionary.items():
        sorted_list.append({'char': char, 'count': entry})

    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list

def print_stats(list, word_count, character_count):

    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {word_count} total words")
    print("\n--------- Character Count -------\n")

    for entry in list:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['count']}\n")

    print("============= END ===============")