# Given a string, return related ASCII code [str, array]

def text_to_ASCII(text: str):
    ASCII_code_string = ''
    ASCII_code_array = []

    for char in text:
        code = ord(char)
        ASCII_code_string += str(code)
        ASCII_code_array.append(str(code))

    return ASCII_code_string, ASCII_code_array
