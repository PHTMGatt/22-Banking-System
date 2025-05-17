# NOTE; Module docstring describing transfer handler purpose
"""This function handles the transfer process for the user."""

# NOTE; Define transfer handler, accepting checking and savings account objects
def handle_transfer(checking, savings):
    """
    Handles the transfer of funds between checking and savings accounts.

    Parameters:
    - checking (Account): The checking account object.
    - savings (Account): The savings account object.
    """
    # NOTE; Prompt user to choose source account or quit
    print("Which account would you like to transfer from?")
    account_choice = input(
        "Enter 1 for checking,\n"
        "enter 2 for savings,\n"
        "enter q to quit: "
    )
    # NOTE; Exit early if user chooses to quit
    if account_choice == 'q':
        return

    try:
        # NOTE; Validate selection is either checking or savings
        if account_choice in ['1', '2']:
            try:
                # NOTE; Prompt for transfer amount and convert to float
                amount = float(input("How much would you like to transfer? "))
            except ValueError:
                # NOTE; Handle non-numeric input and retry
                print("Please enter a dollar amount.\n")
                handle_transfer(checking, savings)
                return

            # NOTE; Perform withdrawal from source and deposit into destination
            if account_choice == '1':
                checking.withdraw(amount)
                savings.deposit(amount)
            else:
                savings.withdraw(amount)
                checking.deposit(amount)

            # NOTE; Display updated balances after transfer
            balances(checking, savings)
        else:
            # NOTE; Invalid menu choice raised as error
            raise ValueError("Invalid choice. Please enter 1, 2, or q.\n")
    except ValueError as e:
        # NOTE; Catch invalid choice error, display message, and retry
        print(e)
        handle_transfer(checking, savings)

# NOTE; Helper function to print both account balances
def balances(checking, savings):
    """This function prints the account balances for the user."""
    print("\nHere are your account balances:")
    print(f"Checking: ${checking.get_balance():,.2f}")
    print(f"Savings:  ${savings.get_balance():,.2f}")
