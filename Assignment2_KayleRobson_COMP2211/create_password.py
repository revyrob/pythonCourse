# Program for creating password
# password must be at least seven characters in length
# password must have at least one uppercase letter, one lowercase letter
# and one digit

def get_password(password):
    # Set boolean variables to false
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    

    # Start testing password length
    if len(password) >= 7:
        correct_length = True

        #Test characters in password
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

    # Determine that all requirements are true
    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    # Return the is_valid variable
    return is_valid

    
    
