# Upload PI value

# PI values site: https://pi2e.ch/blog/2017/03/10/pi-digits-download/

PI_dec_1m_file_name = 'pi_values/pi_dec_1m.txt'
PI_dec_1t_file_name = 'pi_values/pi_dec_1b.txt'
PI_dec_custom_file_name = 'pi_values/pi_dec_custom.txt'

def upload_PI():
    try:
        with open(PI_dec_custom_file_name, 'r') as file:
            text = file.read()
    except:
        try:
            with open(PI_dec_1t_file_name, 'r') as file:
                text = file.read()
        except:
            try:
                with open(PI_dec_1m_file_name, 'r') as file:
                    text = file.read()
            except:
                print("Error. No file wos found in the \"PI values\" folder. Please check there is a file with the PI value.")
                return -1, ''
    
    return 0, text