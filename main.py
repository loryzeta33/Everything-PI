# With this script you can find a number or a word (its relative ASCII code) in the PI value

from upload_pi import upload_pi_value
from utils.text_to_ASCII import text_to_ASCII
from search import search_number_in_pi
from print_result import *


def search_number(pi_string, number):
    # Find number in PI
    match_found, start_index, end_index = search_number_in_pi(pi_string, str(number))

    if match_found:
        print("Good! The number was found in PI!\n")
        print_number(pi_string, start_index, end_index)
    else:
        print("Sorry. The number wasn't found in the PI value.")

def search_text(pi_string, text):
    # Convert word in ASCII code
    ASCII_text = text_to_ASCII(text)

    # Find text in PI
    match_found, start_index, end_index = search_number_in_pi(pi_string, ASCII_text[0])

    if match_found:
        print("Good! The text was found in PI!\n")
        print_text(pi_string, start_index, end_index, ASCII_text[1])
    else:
        print("Sorry. The text wasn't found in the PI value.")

def main():
    try:
        pi_string, file = upload_pi_value()
        print(f"'{file}' pi value uploaded.")
    except FileNotFoundError as e:
        print(e)
        return

    text = str(input("\nWhat do you want to find (type a number or a text)? "))

    try:
        number = eval(text)
        search_number(pi_string, number)
    except Exception:
        search_text(pi_string, text)


if __name__ == '__main__':
    main()
