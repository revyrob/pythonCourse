# A program that shows compound monthly interest
# in a savings account
# prompt the user to enter certain values to come
# to the future value of the account after x
# amount of time

# Break into functions
# Main function asks for all the information needed
def main():
    # Get the amount int he savings account
    savings_balance = float(input('What is the current balance of the savings ' +
                'account: '))
    monthly_interest = float(input('Enter the monthly interest on the ' +
                                     'account: '))
    time_in_account = int(input('How many months will the money be in the ' +
                                'account: '))
    show_savings_plus_interest(savings_balance, monthly_interest, time_in_account)
    
# Function to find the compound interest in the given time
# with the initial savings, period of time, and interest given
def show_savings_plus_interest(savings, interest, time):
    final = savings * (1 + (interest/100))**time
    print('Your total savings will be ${:,.2f}'.format(final),
          ' after ', time, ' months.', sep = '')

# Call main function
main()
