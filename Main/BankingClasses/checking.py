# NOTE; Module docstring for the checking account class
"""The checking account class."""

# NOTE; Import the abstract base class BankAccount
from BankingClasses.banking import BankAccount

# NOTE; Define CheckingAccount as a subclass of BankAccount
class CheckingAccount(BankAccount):
    """
    A class representing a checking account.

    Attributes:
        balance (float): The current balance of the checking account.
        overdraft_limit (float): The maximum negative balance allowed
        for the account.

    Methods:
        __init__(overdraft_limit=100): Initializes a new instance
        of the CheckingAccount class.
        deposit(amount): Deposits the specified amount into the account.
        withdraw(amount): Withdraws the specified amount from the account.
        get_balance(): Returns the current balance of the account.
    """

    # NOTE; Initialize balance and optional overdraft limit (default 100)
    def __init__(self, balance, overdraft_limit=100):
        super().__init__(balance)  # NOTE; Call parent constructor to set balance
        self.overdraft_limit = overdraft_limit  # NOTE; Set overdraft allowance
        self.balance = balance  # NOTE; Initialize balance attribute

    # NOTE; Method to deposit funds into the account
    def deposit(self, amount):
        """ This method deposits the specified amount into the account. """
        self.balance += amount  # NOTE; Increase balance by deposit amount

    # NOTE; Method to withdraw funds from the account
    def withdraw(self, amount):
        """
        This method withdraws the specified amount from the account.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: If the specified amount is greater
            than the allowed balance + overdraft_limit.
        """
        # NOTE; Check if within overdraft limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount  # NOTE; Deduct amount from balance
        else:
            # NOTE; Raise error on insufficient funds
            raise ValueError("Insufficient funds, overdraft limit reached.\n")

    # NOTE; Method to return the current balance
    def get_balance(self):
        """This method returns the current balance of the account."""
        return self.balance  # NOTE; Return balance attribute
