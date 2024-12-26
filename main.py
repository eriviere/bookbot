def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_content(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(book_content)} words found in the document")
    letters_dic = count_each_char(book_content)
    chars_list = sort_by_occurrence(letters_dic)
    for i in range(0, len(chars_list)):
        print(f"The \'{chars_list[i]['name']}\' character was found {chars_list[i]['num']} times")


def get_book_content(book_path):
    with open("books/frankenstein.txt") as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_each_char(text):
    character_list = {}
    for c in text.lower():
        if c in character_list:
            character_list[c] += 1
        else:
            character_list[c] = 1
    return character_list


def sort_on(dict):
    return dict["num"]


def sort_by_occurrence(letters_dic):
    chars_list = []
    for letter in letters_dic:
        if letter.isalpha():
            chars_list.append({"name": letter, "num": letters_dic[letter]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


main()

