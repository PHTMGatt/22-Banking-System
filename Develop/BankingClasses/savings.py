# NOTE; Module docstring for the savings account implementation
"""The savings account class."""

# NOTE; Import the abstract BankAccount base class
from BankingClasses.banking import BankAccount

# NOTE; Define SavingsAccount as a subclass of BankAccount
class SavingsAccount(BankAccount):
    """
    A class representing a savings account.

    Attributes:
        balance (float): The current balance of the savings account.
        overdraft_limit (float): The maximum negative balance allowed.
    """

    # NOTE; Initialize balance and optional overdraft_limit (default 100)
    def __init__(self, balance, overdraft_limit=100):
        super().__init__(balance)  # NOTE; Call parent constructor to set balance
        self.overdraft_limit = overdraft_limit
        self.balance = balance

    # NOTE; Deposit method to add funds to the savings account
    def deposit(self, amount):
        """
        Deposits the specified amount into the savings account.

        Args:
            amount (float): The amount to be deposited.
        """
        self.balance += amount

    # NOTE; Withdraw method to remove funds, respecting the overdraft limit
    def withdraw(self, amount):
        """
        This method withdraws the specified amount from the account.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: If the amount exceeds balance + overdraft_limit.
        """
        # NOTE; Allow withdrawal if within overdraft allowance
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            # NOTE; Deny withdrawal if it would exceed overdraft allowance
            raise ValueError("Insufficient funds, overdraft limit reached.\n")

    # NOTE; Method to return the current account balance
    def get_balance(self):
        """Returns the current balance of the savings account."""
        return self.balance
