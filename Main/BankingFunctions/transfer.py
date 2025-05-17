# NOTE; Module docstring for transfer handler and balance display
""" This module handles fund transfers and displays account balances for the user. """

# NOTE; Define function to transfer funds between checking and savings
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
        "Enter 1 to transfer from checking to savings,\n"
        "enter 2 to transfer from savings to checking,\n"
        "enter q to quit: "
    )
    # NOTE; Exit early if user opts to quit
    if account_choice == 'q':
        return

    try:
        # NOTE; Validate selection is either checking or savings
        if account_choice in ['1', '2']:
            try:
                # NOTE; Prompt for transfer amount and convert to float
                amount = float(input("How much would you like to transfer? "))
            except ValueError:
                # NOTE; Handle non‑numeric input and retry
                print("Please enter a dollar amount.\n")
                handle_transfer(checking, savings)
                return

            # NOTE; Perform withdrawal from source and deposit into destination
            if account_choice == '1':
                checking.withdraw(amount)  # NOTE; Withdraw from checking
                savings.deposit(amount)    # NOTE; Deposit into savings
            else:
                savings.withdraw(amount)   # NOTE; Withdraw from savings
                checking.deposit(amount)   # NOTE; Deposit into checking

            # NOTE; Display updated balances after transfer
            balances(checking, savings)
        else:
            # NOTE; Raise error on invalid menu choice
            raise ValueError("Invalid choice. Please enter 1, 2, or q.\n")
    except ValueError as e:
        # NOTE; Catch invalid choice error, display message, and retry
        print(e)
        handle_transfer(checking, savings)

# NOTE; Helper function to print both account balances
def balances(checking, savings):
    """This function prints the account balances for the user."""
    # NOTE; Header for balance display
    print("\nHere are your account balances:")
    # NOTE; Show checking balance formatted with commas and two decimals
    print(f"Checking: ${checking.get_balance():,.2f}")
    # NOTE; Show savings balance formatted with commas and two decimals
    print(f"Savings:  ${savings.get_balance():,.2f}")
