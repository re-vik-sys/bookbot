import sys

from stats import get_count_of_words

from stats import book_text_to_dict

from stats import chars_dict_to_sorted_list



def get_book_text(get_strings: str) -> str:
    with open(get_strings) as f:
        file_contents = f.read()

    return file_contents


def print_report(book_path, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        character = i[0]
        count = i[1]
        if not character.isalpha():
            continue
        print(f"{character}: {count}")

    print("============= END ===============")


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        book_path_value = (sys.argv)[1]




    book_path_source = get_book_text(book_path_value)


    sum_of_words = get_count_of_words(book_path_source)
    sum_of_strings = book_text_to_dict(book_path_source)
    sorted_output = chars_dict_to_sorted_list(sum_of_strings)


    return print_report(book_path_value, sum_of_words, sorted_output)




main()
