# With this script you can find a number or a word (its relativa ASCII code) in the PI value

# PI values site: https://pi2e.ch/blog/2017/03/10/pi-digits-download/

from colorama import Fore

from upload_PI import upload_PI
from text_to_ASCII import text_to_ASCII
from find_number import find_number
from print_result import *

if __name__ == '__main__':
    mode = 0

    # Uploading PI value
    PI_dec_1m = upload_PI()

    # Ask word to find
    text = str(input("What do you want to find? "))

    try:
        number = eval(text)
    except:
        mode = 1

    # From number
    if mode==0:
        # Find number in PI
        match_found, start_index, end_index = find_number(PI_dec_1m, str(number))

        if match_found:
            print('Good! The number was found in PI!\n')
            print_number(PI_dec_1m, start_index, end_index)
        else:
            print('Sorry. The number wasn\'t found in the PI value.')

    # From text
    else:
        # Convert word in ASCII code
        ASCII_text = text_to_ASCII(text)

        # Find text in PI
        match_found, start_index, end_index = find_number(PI_dec_1m, ASCII_text[0])

        if match_found:
            print('Good! The text was found in PI!\n')
            print_text(PI_dec_1m, start_index, end_index, ASCII_text[1])
        else:
            print('Sorry. The text wasn\'t found in the PI value.')
