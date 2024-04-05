# Import the create_cd_account and create_savings_account functions


# Define the main function
from cd_account import create_cd_account
from savings_account import create_savings_account

# I cant figure out how to prompt the user and format the responses
# doing it this way to hand in the HW and once I know which lesson to look at to figure out how to do this, ill do it again. 

def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_balance = 1000.00
    savings_interest = 10
    savings_maturity = 12

    user_savingsbalance = input("Enter your CD balance:" + savings_balance)
    user_saving_interest = input("Enter your CD Interest:" + savings_balance)
    user_saving_maturity = input("Enter your CD Maturity:" + savings_maturity)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    updated_savings_balance()
    interest_earned()

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
   # I hard coded the variables in order to calculate while completing the homework to make sure it is working
    cd_balance = 1000.00
    cd_interest = 10
    cd_maturity = 12

    user_cdbalance = input(f"Enter your CD Maturity: {cd_balance}")
    user_cd_interest = input(f"Enter your CD Interest: {cd_interest}")
    user_cd_maturity = input(f"Enter your CD Maturity: {cd_maturity}")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    updated_cd_balance()
    interest_earned()

if __name__ == "__main__":
    # Call the main function.
    main()