# NOTE; Module docstring for the main banking application
"""This function handles the transfer process for the user."""

# NOTE; Import account classes and validation utility
from BankingClasses.checking import CheckingAccount
from BankingClasses.savings import SavingsAccount
from BankingClasses.validation import Validation

# NOTE; Import banking operation functions
from BankingFunctions.deposit import handle_deposit
from BankingFunctions.withdraw import handle_withdrawal
from BankingFunctions.transfer import handle_transfer, balances

# NOTE; Entry point of the banking system
def main():
    """
    This function is the entry point of the banking system.
    It prompts for user credentials, validates them, initializes accounts,
    and provides a menu for deposit, withdrawal, transfer, and balance checks.
    """
    # NOTE; Prompt for email and password
    email = input("Enter your email: ")
    print(
        "Your password should be at least 8 characters long,\n"
        "contain at least one uppercase and lowercase letter,\n"
        "one number, and one of the following special characters:!@#$%^&*."
    )
    password = input("Enter your password: ")

    # NOTE; Initialize login attempt counter
    attempts = 1
    # NOTE; Allow up to 3 attempts for correct credentials
    while attempts < 3:
        # NOTE; Validate email format and password strength
        if not Validation.validate_email(email) or not Validation.validate_password(password):
            print("\nInvalid email or password. Please try again.")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            attempts += 1
        else:
            # NOTE; Break if validation succeeds
            break

    # NOTE; Exit if maximum attempts reached
    if attempts == 3:
        print("Maximum number of attempts reached. Exiting program.")
        return

    # NOTE; Initialize accounts with default balances
    checking_account = CheckingAccount(4321.00)
    savings_account = SavingsAccount(6543.21)

    # NOTE; Display initial balances
    print("\nHere are your account balances:")
    print(f"Checking: ${checking_account.get_balance():,.2f}")
    print(f"Savings:  ${savings_account.get_balance():,.2f}")

    # NOTE; Main menu loop for banking operations
    while True:
        print("\nWhat would you like to do?")
        print("Make a deposit? Enter 1")
        print("Make a withdrawal? Enter 2")
        print("Make a transfer? Enter 3")
        print("Check account balances? Enter 4")
        print("Quit? Enter q\n")
        choice = input("Enter your choice: ")

        # NOTE; Validate menu choice
        if choice in ['1', '2', '3', '4', 'q']:
            if choice == '1':
                # NOTE; Handle deposit
                handle_deposit(checking_account, savings_account)
            elif choice == '2':
                # NOTE; Handle withdrawal
                handle_withdrawal(checking_account, savings_account)
            elif choice == '3':
                # NOTE; Handle transfer
                handle_transfer(checking_account, savings_account)
            elif choice == '4':
                # NOTE; Display balances
                balances(checking_account, savings_account)
            elif choice == 'q':
                # NOTE; Exit program
                break
        else:
            # NOTE; Handle invalid menu selection
            print("Invalid choice. Please enter 1, 2, 3, 4, or q.\n")

# NOTE; Execute main function when run as a script
if __name__ == "__main__":
    main()
