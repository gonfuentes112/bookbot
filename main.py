def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(s):
    return len(s.split())

def count_letters(s):
    letter_dict = {}
    for letter in s:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def sort_on(dict):
    return dict["count"]

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report = [{"char": key, "count":value} for key, value in count_letters(text).items()]
    report.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    amount_words = count_words(text)
    print(f"{amount_words} words found in the document")
    for pair in report:
        char, count = pair["char"], pair["count"]
        print(f"The \'{char}\' character was found {count} times.")
    print("--- End report ---")
main()