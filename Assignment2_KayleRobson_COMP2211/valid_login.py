# Program main where the information from the student is obtained
# Call the function get obtain a login name after info is imported
# then the student's login name is returned as a string
#
# Get the user to enter a password
# Call the password function
# return of the password is valid or invalid

import create_password
import create_username
import sys

def main():

    try:
        
        # Student's first name
        # While loop created to catch names less than 3 letters and spaces
        first_name = input("What is your first name? ")
        while (len(first_name) < 3) or (' ' in first_name):
            print("First name must be at least 3 characters with no spaces")
            first_name = input("What is your first name? ")

        # Student's last name
        # While loop created to catch names less than 3 letters and spaces
        last_name = input("What is your last name? ")
        while (len(last_name) < 3) or (' ' in last_name):
            print("Last name must be at least 3 characters with no spaces")
            last_name = input("What is your last name? ")

        # Student's ID
        # While loop created to catch id less than 3 letters and spaces
        stu_id = input("What is your student ID? ")
        while (len(stu_id) < 3) or (' ' in stu_id):
            print("Student ID must be at least 3 characters with no spaces")
            stu_id = input("What is your student ID? ")

        # Print the username created for the user
        # I put it all in caps since it looks more fluid as a user name
        userName = create_username.get_login_name(first_name, last_name, stu_id)
        print("Your user name is " + userName.upper())
    
        # Get password from user
        password = input("Enter your password: ")
    
        # Call the get_login function
        while not create_password.get_password(password):
            print("That is not a valid password.")
            password = input("Enter your password: ")
        print("That is a valid password.")

    except:
            print("You have encountered an error.")

def error(message):
    sys.stderr.write("error: %s\n" % message)
    sys.exis(1)

# Call main
main()

    
