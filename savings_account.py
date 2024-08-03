"""Import the Account class from the Account.py file."""
from Account import Account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
  
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    savingsaccount = Account(balance,0)

    # Calculate interest earned
    interest_earned = balance * (interest_rate/100 * months/12)

    # Update the savings account balance by adding the interest earned
    updated_savingbalance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    savingsaccount.set_balance(updated_savingbalance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    savingsaccount.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return  updated_savingbalance, interest_earned
