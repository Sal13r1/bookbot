from stats import count_words, count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    text = get_book_text('books/frankenstein.txt')
    count_words(text)
    count_letters(text)
    

if __name__ == '__main__':
    main()