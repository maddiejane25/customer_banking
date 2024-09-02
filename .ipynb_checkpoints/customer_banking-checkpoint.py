# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = int(input("What is the savings balance?"))
    interest_rate = int(input("What is the interest rate?"))
    months = int(input("For how many months?"))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, interest_rate, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Interest earned:" [savings_account.interest_earned])
    print("Updated savings account balance:" [savings_account.updated_savings_balance])

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    CD_balance = int(input("What is the CD balance"))
    interest_rate = int(input("What is the interest rate?"))
    CD_months = int(input("For how many months?"))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, interest_rate, CD_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Interest earned:" [cd_account.interest_earned])
    print("Updated CD account balance:" [cd_account.updated_cd_balance])

if __name__ == "__main__":
    # Call the main function.
        main()