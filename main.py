from stats import count_words, count_letters, sort_stats, print_stats
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():

    if len(sys.argv) > 1:
        print("First argument:", sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    directory = "./" + sys.argv[1]
    text = get_book_text(directory)
    word_count = count_words(text)
    character_count = count_letters(text)

    sorted_list = sort_stats(character_count)
    print_stats(sorted_list, word_count, character_count)
    

if __name__ == '__main__':
    main()