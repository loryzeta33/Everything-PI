# Find given number in PI

def search_number_in_pi(pi_value: str, value: str):
    pi_index = 0
    value_index = 0
    value_length = len(value)
    pi_length = len(pi_value)

    start_index = 0
    end_index = 0

    match_found = False

    while True:

        # Start matching
        if pi_value[pi_index] == value[value_index]:

            # Set starting point
            if value_index == 0:
                start_index = pi_index
            
            # Check if it is the last value index
            if value_index == (value_length-1):
                match_found = True
                end_index = pi_index
            
            # Exit loop if match is found
            if match_found:
                break

            # Update value index
            value_index += 1
        else:
            # Reset value index
            if value_index != 0:
                pi_index = start_index
            value_index = 0

        # End of PI
        if pi_index == (pi_length-1):
            break

        # Increment PI index
        pi_index += 1
    
    return match_found, start_index, end_index
