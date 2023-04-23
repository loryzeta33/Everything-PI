from colorama import Fore

def print_text(PI_value: str, start_index: int, end_index: int, text_array: tuple[str]):
    for index in range(0,25):
        print(PI_value[index], end='')
    
    print(' ... ', end='')

    for index in range(start_index-10,start_index):
        print(PI_value[index], end='')
    print(' ', end='')

    for code in text_array:
        print(Fore.MAGENTA + code + ' ', end='')
    print(Fore.RESET + '', end='')
    
    for index in range(end_index+1,end_index+11):
        print(PI_value[index], end='')
    
    print('...')

    print('\nFirst index: ', start_index)
    print('Last index: ', end_index)


def print_number(PI_value: str, start_index: int, end_index: int):
    for index in range(0,25):
        print(PI_value[index], end='')
    
    print(' ... ', end='')

    for index in range(start_index-10,start_index):
        print(PI_value[index], end='')
    print(' ', end='')

    for index in range(start_index,end_index+1):
        print(Fore.MAGENTA + PI_value[index], end='')
    print(Fore.RESET + ' ', end='')
    
    for index in range(end_index+1,end_index+11):
        print(PI_value[index], end='')
    
    print('...')

    print('\nFirst index: ', start_index)
    print('Last index: ', end_index)