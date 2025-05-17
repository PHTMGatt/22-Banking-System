# NOTE; Module docstring describing the purpose of this class
""" This class validates the email addresses and password when logging on."""

# NOTE; Define Validation utility class with static methods
class Validation:
    """ This class contains methods for validating email addresses and passwords."""

    @staticmethod
    # NOTE; Validate that an email contains an "@" symbol
    def validate_email(email):
        return "@" in email

    @staticmethod
    # NOTE; Validate password complexity and length
    def validate_password(password):
        """
        This method validates a password based on the following criteria:
        - The password must be at least 8 characters long.
        - The password must contain at least one uppercase letter,
          one lowercase letter, one digit, and one special character (!@#$%^&*).

        Args:
          password (str): The password to be validated.

        Returns:
          bool: True if the password is valid, False otherwise.
        """
        # NOTE; Reject passwords shorter than 8 characters immediately
        if len(password) < 8:
            return False

        # NOTE; Initialize flags for each required character type
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        special_characters = "!@#$%^&*"

        # NOTE; Iterate through each character and set flags accordingly
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_characters:
                has_special = True

        # NOTE; Return True only if all criteria are met
        return has_upper and has_lower and has_digit and has_special
