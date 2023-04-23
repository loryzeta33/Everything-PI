# Find given number in PI

def find_number(PI_value: str, value: str):
    PI_index = 0
    value_index = 0
    value_lenght = len(value)
    PI_lenght = len(PI_value)

    start_index = 0
    end_index = 0

    match_found = False

    while True:

        # Start matching
        if PI_value[PI_index]==value[value_index]:

            # Set start point
            if value_index==0:
                start_index = PI_index
            
            # Check if it is the last value index
            if value_index==(value_lenght-1):
                match_found = True
                end_index = PI_index
            
            # Exit loop if match is found
            if match_found:
                break

            # Update value index
            value_index += 1
        else:
            # Reset value index
            value_index = 0
        
        if PI_index==(PI_lenght-1):
            break

        # Increment PI index
        PI_index += 1
    
    return match_found, start_index, end_index
