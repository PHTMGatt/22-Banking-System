# NOTE; Module docstring for the savings account class
"""The savings account class."""

# NOTE; Import the abstract base class BankAccount
from BankingClasses.banking import BankAccount

# NOTE; Define SavingsAccount as a subclass of BankAccount
class SavingsAccount(BankAccount):
    """
    A class representing a savings account.

    Attributes:
        balance (float): The current balance of the savings account.
        overdraft_limit (float): The maximum negative balance allowed for the account.
    """

    # NOTE; Initialize balance and optional overdraft limit (default 100)
    def __init__(self, balance, overdraft_limit=100):
        super().__init__(balance)               # NOTE; Call parent constructor to set balance
        self.overdraft_limit = overdraft_limit  # NOTE; Set overdraft allowance
        self.balance = balance                  # NOTE; Initialize balance attribute

    # NOTE; Method to deposit funds into the savings account
    def deposit(self, amount):
        """Deposits the specified amount into the savings account."""
        self.balance += amount                  # NOTE; Increase balance by deposit amount

    # NOTE; Method to withdraw funds, respecting overdraft limit
    def withdraw(self, amount):
        """
        Withdraws the specified amount from the savings account.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: If the amount exceeds balance + overdraft_limit.
        """
        # NOTE; Allow withdrawal if within overdraft allowance
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount              # NOTE; Deduct amount from balance
        else:
            # NOTE; Raise error on insufficient funds
            raise ValueError("Insufficient funds, overdraft limit reached.\n")

    # NOTE; Method to return the current account balance
    def get_balance(self):
        """Returns the current balance of the savings account."""
        return self.balance                     # NOTE; Return balance attribute
