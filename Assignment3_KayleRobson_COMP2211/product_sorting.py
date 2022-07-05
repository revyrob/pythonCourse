# Company program for sorting product codes
# function to validate codes
# function to find out if there are any restrictions

import valid_codes
import invalid_codes
import restricted_codes

def main():

    # Inform the user what the program does
    print("Hello!")
    print("This program will process the company codes within 'Codes.txt'.")
    print("You will find this in the same directory as the program.")
    print("Please update codes in 'Codes.txt' to test new codes.")
    print("A valid code consists of: ")
    print("1) 10 digits before before the hyphanted number code.")
    print("2) Position 10 is letter")
    print("3) Position 4 to 7 can only be digits.")
    print("Example valid code: ABC1234UIO-14")
    print("After the code has been validated.")
    print("The program will determine if the code is restricted.")
    print("Restriction will be indicated with an 'R' in the 10th positon")
    print("Restricted items are not allowed in country codes 2000 or more.")
    print("Once the program has iterated over the code a list will be printed.")
    print("The list will be called 'sorted_codes.txt'.")
    print("The list will have 3 headings: Valid Code(s), Invalid Code(s)\n" +
          "Restricted Code(s)")
    print('\n')
    print('\n')

    try:
        # Read product codes from text file
        infile = open("Codes.txt", "r")
        file_contents = infile.read()
        # Split list with \n to get a good list to iterate over
        company_codes = file_contents.split('\n')

        # my functions to lists
        invalid = invalid_codes.get_invalid(company_codes)
        valid = valid_codes.get_valid(company_codes)
        restricted = restricted_codes.get_restricted(valid)
   

        # Loop to write code
        with open('sorted_codes.txt', 'w') as sorted_codes:

            sorted_codes.write('Valid Codes(s)\n')
            sorted_codes.write('--------------\n')
            for item in valid:
                sorted_codes.write('%s\n' %item)

            sorted_codes.write('\n')
            sorted_codes.write('Invalid Codes(s)\n')
            sorted_codes.write('--------------\n')
            for item in invalid:
                sorted_codes.write('%s\n' %item)

            sorted_codes.write('\n')
            sorted_codes.write('Restricted Codes(s)\n')
            sorted_codes.write('--------------\n')
            for item in restricted:
                sorted_codes.write('%s\n' %item)
        print('File printed to sorted_codes.txt')

    except Exception as e:
        print("Exception!!")
        print(e)
        
    finally:
        # Close the file that was being read
        infile.close()
        sorted_codes.close()
        print('File closed')    

# Call main
main()


