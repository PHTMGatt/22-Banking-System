# NOTE; Module docstring describing withdrawal handler purpose
"""This function handles the withdrawal process for the user."""

# NOTE; Define withdrawal handler, accepting checking and savings account objects
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
        "enter 2 for savings.\n"
        "enter q to quit: "
    )
    # NOTE; Exit early if user chooses to quit
    if account_choice == 'q':
        return

    try:
        # NOTE; Validate selection is either checking or savings
        if account_choice in ['1', '2']:
            try:
                # NOTE; Prompt for withdrawal amount and convert to float
                amount = float(input("Enter the amount to withdraw: "))
            except ValueError:
                # NOTE; Handle non‑numeric input and retry
                print("Invalid amount. Please enter a valid dollar amount.")
                handle_withdrawal(checking, savings)
                return

            # NOTE; Perform withdrawal on chosen account and display updated balance
            if account_choice == '1':
                checking.withdraw(amount)
                # NOTE; Show updated checking balance formatted with commas and two decimals
                print(f"Here is your checking balance: ${checking.get_balance():,.2f}")
            else:
                savings.withdraw(amount)
                # NOTE; Show updated savings balance formatted with commas and two decimals
                print(f"Here is your savings balance: ${savings.get_balance():,.2f}")
        else:
            # NOTE; Invalid menu choice raised as error
            raise ValueError("Invalid choice. Please enter 1, 2, or q.\n")
    except ValueError as e:
        # NOTE; Catch invalid choice error, display message, and retry
        print(e)
        handle_withdrawal(checking, savings)
