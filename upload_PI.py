# Upload PI value

PI_dec_1m_file_name = 'PI values/pi_dec_1m.txt'
PI_dec_1t_file_name = 'PI values/pi_dec_1t.txt'

def upload_PI():
    try:
        with open(PI_dec_1t_file_name, 'r') as file:
            text = file.read()
    except:
        with open(PI_dec_1m_file_name, 'r') as file:
            text = file.read()
    
    return text