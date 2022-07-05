# Program that has a creates a students ID
# Get the first three characters of the Student's first name
# Get the first three characters of the Student's last name
# Get the last three characters of the Student's ID
# Concatenate the three sets of characters to generate a name
# Catch errors


def get_login_name(first_name, last_name, stu_id):
    # Get the first three letters of the first name
    set1 = first_name[0:3]

    # Get the first three letters of the last name
    set2 = last_name[0:3]

    # Get the last three characters of the student ID
    set3 = stu_id[-3:]

    # Put the sets of characters together
    login_name = set1 + set2 + set3

    # Return the login name
    return login_name
