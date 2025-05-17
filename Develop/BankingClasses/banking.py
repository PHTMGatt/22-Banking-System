# NOTE; Module docstring describing the purpose of this module
""" This module contains the abstract base class for a bank account. """

# NOTE; Import Abstract Base Class machinery
from abc import ABC, abstractmethod

# NOTE; Define the abstract BankAccount class
class BankAccount(ABC):
    """
    Abstract base class representing a bank account.

    Attributes:
        balance (float): The current balance of the bank account.

    Methods:
        deposit(amount): Deposits the specified amount into the bank account.
        withdraw(amount): Withdraws the specified amount from the bank account.
        get_balance(): Returns the current balance of the bank account.
    """

    # NOTE; Initialize account with optional starting balance
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    # NOTE; Abstract deposit method to add funds
    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        pass

    @abstractmethod
    # NOTE; Abstract withdraw method to remove funds
    def withdraw(self, amount):
        """Withdraws the specified amount from the account."""
        pass

    @abstractmethod
    # NOTE; Abstract method to return current balance
    def get_balance(self):
        """Gets the balance of the specified account."""
        pass
