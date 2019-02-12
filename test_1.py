while True:
    user_ssn_number = input('Enter your SSN number in format (0000):')
    if len(user_ssn_number) !=4:
        print('Invalod SSn, please check format')
        continue

