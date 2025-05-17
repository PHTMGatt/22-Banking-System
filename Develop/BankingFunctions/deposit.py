# NOTE; Function docstring explaining deposit handler purpose
"""This function handles the deposit process for the user."""

def handle_deposit(checking, savings):
    # NOTE; Prompt user to choose account or quit
    print("Which account would you like to make a deposit?")
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
                # NOTE; Prompt for deposit amount and convert to float
                amount = float(input("How much would you like to deposit? "))
            except ValueError:
                # NOTE; Handle non-numeric input and retry
                print("Please enter a dollar amount.\n")
                handle_deposit(checking, savings)
                return

            # NOTE; Perform deposit on the chosen account
            if account_choice == '1':
                checking.deposit(amount)
                # NOTE; Show updated checking balance formatted with commas and two decimals
                print(f"Here is your checking balance: ${checking.get_balance():,.2f}")
            else:
                savings.deposit(amount)
                # NOTE; Show updated savings balance formatted with commas and two decimals
                print(f"Here is your savings balance: ${savings.get_balance():,.2f}")
        else:
            # NOTE; Invalid menu choice
            raise ValueError("Invalid choice. Please enter 1, 2, or q.\n")

    except ValueError as e:
        # NOTE; Catch invalid choice error, display message, and retry
        print(e)
        handle_deposit(checking, savings)
