# Customer Banking (Saving, CD Account Interest Calculator)

This project consists of four Python files that together form a simple banking system to manage and calculate the balance and interest earned on Savings and Certificate of Deposit (CD) accounts. Below is a summary of each file and how they interact with each other.

# File 1: Account.py 
> This file defines the Account class, which includes methods to set the balance and interest for an account.
```
class Account:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        self.balance = balance

    def set_interest(self, interest):
        self.interest = interest
```

# File 2: cd_account.py
> This file imports the Account class from Account.py and defines a function create_cd_account that creates a CD account, calculates the interest earned, and updates the account balance.

```
from Account import Account

def create_cd_account(balance, interest_rate, months):
    cd_account = Account(balance, 0)
    interest_earned = balance * (interest_rate / 100 * months / 12)

    updated_cd_balance = balance + interest_earned
    cd_account.set_balance(updated_cd_balance)
    cd_account.set_interest(interest_earned)

    return updated_cd_balance, interest_earned
```

# File 3: customer_banking.py
> This file imports functions from cd_account.py and savings_account.py and contains the main function that prompts the user for input, creates savings and CD accounts, and displays the updated balances and interest earned.

```
from cd_account import create_cd_account
from savings_account import create_savings_account

def main():
    savings_balance = float(input("What is your current savings balance? "))
    savings_interest = float(input("What is the interest rate for your savings account? "))
    savings_maturity = float(input("Enter length of months to determine interest: "))
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print('Your updated savings account balance with interest earned is $', format(updated_savings_balance, ',.2f'))

    cd_balance = float(input("What is your current CD balance? "))
    cd_interest = float(input("What is the interest rate for your CD account? "))
    cd_maturity = int(input("Enter length of months to determine interest: "))
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    print('Your updated CD account balance with interest earned is $', format(updated_cd_balance, ',.2f'))

if __name__ == "__main__":
    main()

```

# File 4: savings_account.py
> This file imports the Account class from Account.py and defines a function create_savings_account that creates a savings account, calculates the interest earned, and updates the account balance.

from Account import Account
```
def create_savings_account(balance, interest_rate, months):

    savings_account = Account(balance, 0)
    interest_earned = balance * (interest_rate / 100 * months / 12)
    updated_saving_balance = balance + interest_earned
    savings_account.set_balance(updated_saving_balance)
    savings_account.set_interest(interest_earned)

    return updated_saving_balance, interest_earned
```

# Summary of How Files Work Together

1. Account.py: Defines the Account class with methods to set the balance and interest.
2. cd_account.py: Utilizes the Account class to create and manage a CD account, calculating and updating interest.
3. savings_account.py: Utilizes the Account class to create and manage a savings account, calculating and updating interest.
4. customer_banking.py: Acts as the main entry point, prompting user input to create and manage both savings and CD accounts, displaying the updated balances and interest earned by calling functions from cd_account.py and savings_account.py.
> Together, these files form a simple but functional banking application that allows users to manage their savings and CD accounts, calculating and displaying the interest earned over a specified period.
