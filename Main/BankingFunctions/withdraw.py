# NOTE; Module docstring for withdrawal handler
"""This function handles the withdrawal process for the user."""

# NOTE; Define function to handle withdrawals from checking or savings
def handle_withdrawal(checking, savings):
    """
    Handles the withdrawal of funds for checking and savings accounts.

    Parameters:
    - checking (CheckingAccount): The checking account object.
    - savings (SavingsAccount): The savings account object.
    """
    # NOTE; Prompt user to choose account or quit
    print("Which account would you like to make a withdrawal?")
    account_choice = input(
        "Enter 1 for checking,\n"
        "enter 2 for savings,\n"
        "enter q to quit: "
    )
    # NOTE; Exit early if user opts to quit
    if account_choice == 'q':
        return

    try:
        # NOTE; Validate selection is either checking or savings
        if account_choice in ['1', '2']:
            try:
                # NOTE; Prompt for withdrawal amount and convert to float
                amount = float(input("How much would you like to withdraw? "))
            except ValueError:
                # NOTE; Handle non‑numeric input and retry
                print("Please enter a dollar amount.\n")
                handle_withdrawal(checking, savings)
                return

            # NOTE; Perform withdrawal on selected account and show updated balance
            if account_choice == '1':
                checking.withdraw(amount)  # NOTE; Withdraw from checking
                print(f"Here is your checking balance: ${checking.get_balance():,.2f}")
            else:
                savings.withdraw(amount)   # NOTE; Withdraw from savings
                print(f"Here is your savings balance: ${savings.get_balance():,.2f}")
        else:
            # NOTE; Raise error on invalid menu choice
            raise ValueError("Invalid choice. Please enter 1, 2, or q.\n")
    except ValueError as e:
        # NOTE; Catch invalid choice error, display message, and retry
        print(e)
        handle_withdrawal(checking, savings)
        return
