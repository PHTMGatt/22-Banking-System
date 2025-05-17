# NOTE; Module docstring for the abstract bank account base class
""" This module contains the abstract base class for a bank account. """

# NOTE; Import Abstract Base Class utilities from the standard library
from abc import ABC, abstractmethod

# NOTE; Define the abstract BankAccount class, enforcing deposit/withdraw/get_balance
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

    # NOTE; Initialize a new bank account, defaulting balance to 0
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    # NOTE; Abstract method signature for depositing funds
    def deposit(self, amount):
        """Deposits the specified amount into the account."""

    @abstractmethod
    # NOTE; Abstract method signature for withdrawing funds
    def withdraw(self, amount):
        """Withdraws the specified amount into the account."""

    @abstractmethod
    # NOTE; Abstract method signature for retrieving the balance
    def get_balance(self):
        """Gets the balance of the specified account."""
