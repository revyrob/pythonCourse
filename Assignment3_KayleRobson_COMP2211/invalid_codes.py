# Function for an invalid code in company codes list
# invalid code is:
# less than a 10 characters
# position 10 is not a letter
# position 4 to 7 contains items other than digits

def get_invalid(company_codes):
    # For loop to iterate over codes in array list
    # if valid these codes are under 'Valid Code(s)'
    # if they are not valid they are under 'Invalid Code(s)'
    valid = []
    invalid = []
    for c in company_codes:
        security = c[9:10]
        country = c[3:7]
        if (len(c) >= 10) and (security.isalpha()) and (country.isdigit()):
            valid.append(c)
        else:
            invalid.append(c)
    return invalid
