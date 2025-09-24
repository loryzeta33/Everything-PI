from colorama import Fore


FIRST_DIGITS = 25
LATERAL_DIGITS = 10


def _get_prefix_and_suffix(pi_value: str, start_index: int, end_index: int):
    return pi_value[0:FIRST_DIGITS] + " ... " + pi_value[start_index-LATERAL_DIGITS:start_index] + " ", pi_value[end_index+1:end_index+LATERAL_DIGITS+1] + "..."

def print_text(pi_value: str, start_index: int, end_index: int, text_array: tuple[str]):
    prefix, suffix = _get_prefix_and_suffix(pi_value, start_index, end_index)

    if start_index < FIRST_DIGITS:
        prefix = pi_value[0:start_index] + " "

    if end_index >= len(pi_value)-LATERAL_DIGITS-1:
        suffix = pi_value[end_index+1:]

    pi_string = ""
    for code in text_array:
        pi_string += Fore.MAGENTA + code + " "
    pi_string += Fore.RESET

    print(prefix + pi_string + suffix)

    print('\nFirst index: ', start_index)
    print('Last index: ', end_index)


def print_number(pi_value: str, start_index: int, end_index: int):
    prefix, suffix = _get_prefix_and_suffix(pi_value, start_index, end_index)

    if start_index < FIRST_DIGITS:
        prefix = pi_value[0:start_index] + " "

    if end_index >= len(pi_value)-LATERAL_DIGITS-1:
        suffix = pi_value[end_index+1:]

    pi_string = Fore.MAGENTA + pi_value[start_index:end_index+1] + Fore.RESET + " "

    print(prefix + pi_string + suffix)

    print('\nFirst index: ', start_index)
    print('Last index: ', end_index)