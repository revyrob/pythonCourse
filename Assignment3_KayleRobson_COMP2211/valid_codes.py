# Function for an valid code in company codes list
# valid code is:
# greater than a length of 10
# position 10 is a letter
# position 4 to 7 contains items digits

def get_valid(company_codes):
    # For loop to iterate over codes in array list
    # if valid these codes are under 'Valid Code(s)'
    # if they are not valid they are under 'Invalid Code(s)'
    valid = []
    for c in company_codes:
        security = c[9:10]
        country = c[3:7]
        if (len(c) >= 10) and (security.isalpha()) and (country.isdigit()):
            valid.append(c)
    return valid
