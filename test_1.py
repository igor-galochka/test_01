while True:
    user_ssn_number = input('Enter your SSN number in format (0000):')
    if len(user_ssn_number) !=4:
        print('Invalod SSn, please check format')
        continue

    if not user_ssn_number.isdigit():
        print('fgfgfgfgf')
        continue
# fgdfgdfgdf
    if int(user_ssn_number) not in SSN_white_list:
        print('ghhghhhghg')
        continue


