def check_password(pwd):
    # Password rules
    max_16_chars = False
    min_8_chars = False
    min_1_uppercase = False
    min_1_lowercase = False
    min_1_number = False
    min_1_special = False
    special_char_string = '\'~!#$%^*()_+-={}|[]\\:<>?,./'
    
    # Checking if password meets the criteria
    if (len(pwd) >= 8) and (len(pwd) <= 16):
        max_16_chars = True 
        min_8_chars = True
    else:
        return False
    for letter in pwd:
        if letter.isupper(): 
            min_1_uppercase = True 
        if letter.islower():
            min_1_lowercase = True
        if letter.isdigit():
            min_1_number = True
        if letter in special_char_string:
            min_1_special = True
        # All rules must be satisfied for valid password
        if max_16_chars and min_8_chars and min_1_uppercase and min_1_lowercase and min_1_number and min_1_special:
            return True
    return False


password = input('Enter your password: ')

if check_password(password):
    print('Your password is valid.')
else:
    print('Your password is not valid.')
