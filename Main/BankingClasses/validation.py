# NOTE; Module docstring describing the validation functionality
""" This class validates the email addresses and password when logging on."""

class Validation:
    """ This class contains methods for validating email addresses and passwords."""
    
    @staticmethod
    # NOTE; Static method to validate email addresses by checking for "@" symbol
    def validate_email(email):
        """ This function validates an email address."""
        return "@" in email

    @staticmethod
    # NOTE; Static method to validate password complexity and length
    def validate_password(password):
        """
        This function validates a password based on the following criteria:
        - The password must be at least 8 characters long.
        - The password must contain at least one uppercase letter,
        - one lowercase letter, one digit, and one special character(!@#$%^&*).

        Args:
          password (str): The password to be validated.

        Returns:
          bool: True if the password is valid, False otherwise.
        """
        # NOTE; Reject if password shorter than 8 characters
        if len(password) < 8:
            return False

        # NOTE; Initialize flags for each required character type
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        special_characters = "!@#$%^&*"

        # NOTE; Iterate through password to set flags
        for char in password:
            if char.isupper():
                # NOTE; Uppercase letter found
                has_upper = True
            elif char.islower():
                # NOTE; Lowercase letter found
                has_lower = True
            elif char.isdigit():
                # NOTE; Digit found
                has_digit = True
            elif char in special_characters:
                # NOTE; Special character found
                has_special = True

        # NOTE; Return True only if all criteria are satisfied
        return has_upper and has_lower and has_digit and has_special
