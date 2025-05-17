# NOTE; Module docstring for the main banking application
"""This function handles the transfer process for the user."""

# NOTE; Import account classes and validation utilities
from BankingClasses.checking import CheckingAccount
from BankingClasses.savings import SavingsAccount
from BankingClasses.validation import Validation

# NOTE; Import banking operation functions
from BankingFunctions.deposit import handle_deposit
from BankingFunctions.withdraw import handle_withdrawal
from BankingFunctions.transfer import handle_transfer, balances

def main():
    """
    This function is the entry point of the banking system.
    It prompts the user to enter their email and password for authentication.
    If the email and password are valid, the default balances are shown.
    It then presents a menu of options to the user,
    allowing them to make deposits, withdrawals, or transfers between accounts.
    """
    # NOTE; Prompt for user credentials
    email = input("Enter your email: ")
    print("Your password should be at least 8 characters long,\n"
           "contain at least one uppercase and lowercase letter,\n"
           "one number, and one of the following special characters:!@#$%^&*.")
    password = input("Enter your password: ")

    # NOTE; Initialize attempt counter
    attempts = 1
    # NOTE; Allow up to 3 authentication attempts
    while attempts < 3:
        # NOTE; Validate email and password format
        if not Validation.validate_email(email) or not Validation.validate_password(password):
            print("Invalid email or password. Please try again.")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            attempts += 1
        else:
            # NOTE; Exit loop if credentials are valid
            break

    # NOTE; Exit if maximum attempts exceeded
    if attempts > 3:
        print("Maximum number of attempts reached. Exiting program.")
        return

    # NOTE; Initialize accounts with default balances
    checking_account = CheckingAccount(4321.00)
    savings_account = SavingsAccount(6543.21)

    # NOTE; Display initial account balances
    print("\nHere are your account balances:")
    print(f"Checking: ${checking_account.get_balance():,.2f}")
    print(f"Savings: ${savings_account.get_balance():,.2f}")

    # NOTE; Main menu loop for banking operations
    while True:
        print("\nWhat would you like to do?")
        print("Make a deposit? Enter 1")
        print("Make a withdrawal? Enter 2")
        print("Make a transfer? Enter 3")
        print("Check account balances? Enter 4")
        print("Quit? Enter q\n")
        choice = input("Enter your choice: ")

        # NOTE; Process user choice if valid
        if choice in ['1', '2', '3', '4', 'q']:
            if choice == '1':
                handle_deposit(checking_account, savings_account)   # NOTE; Deposit flow
            elif choice == '2':
                handle_withdrawal(checking_account, savings_account)  # NOTE; Withdrawal flow
            elif choice == '3':
                handle_transfer(checking_account, savings_account)  # NOTE; Transfer flow
            elif choice == '4':
                balances(checking_account, savings_account)  # NOTE; Display balances
            elif choice == 'q':
                break  # NOTE; Exit program
        else:
            # NOTE; Handle invalid menu selection
            print("Invalid choice.  Please re-enter\n")

if __name__ == "__main__":
    main()  # NOTE; Run the main program entry point
