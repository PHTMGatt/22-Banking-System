# NOTE; Module docstring for the checking account implementation
"""The checking account class."""

# NOTE; Import the abstract BankAccount base class
from BankingClasses.banking import BankAccount

# NOTE; Define CheckingAccount as a subclass of BankAccount
class CheckingAccount(BankAccount):
    """
    A class representing a checking account.

    Attributes:
        overdraft_limit (float): The maximum negative balance allowed.
        balance (float): The current balance of the account.
    """

    # NOTE; Initialize balance and optional overdraft_limit (default 100)
    def __init__(self, balance, overdraft_limit=100):
        super().__init__(balance)  # NOTE; Call parent constructor to set balance
        self.overdraft_limit = overdraft_limit
        self.balance = balance

    # NOTE; Deposit method to add funds to the account
    def deposit(self, amount):
        """This method deposits the specified amount into the account."""
        self.balance += amount

    # NOTE; Withdraw method to remove funds, respecting overdraft limit
    def withdraw(self, amount):
        """
        This method withdraws the specified amount from the account.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: If the amount exceeds balance + overdraft_limit.
        """
        # NOTE; Allow withdrawal if within overdraft limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            # NOTE; Deny withdrawal if it would exceed overdraft allowance
            raise ValueError("Insufficient funds, overdraft limit reached.\n")

    # NOTE; Method to return the current account balance
    def get_balance(self):
        """Returns the current balance of the checking account."""
        return self.balance
