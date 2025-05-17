# Banking System CLI App

A simple command-line banking application built with Python OOP principles.  
Users can securely log in, view checking and savings balances, make deposits, withdrawals, and transfers between accounts.

---

## Features

- **User Authentication**  
  - Email validation (`@` symbol)  
  - Password complexity: minimum 8 chars, uppercase, lowercase, digit, special character

- **Account Management**  
  - View current balances for Checking and Savings  
  - Deposit funds into either account  
  - Withdraw funds with overdraft protection (up to \$100)  
  - Transfer funds between Checking and Savings

- **Robust Input Handling**  
  - Recursive prompts on invalid choices  
  - Formatted currency output (commas + two decimals)  
  - Maximum 3 login attempts

---

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/banking-system-cli.git
   cd banking-system-cli
   ```

2. (Optional) Create and activate a virtual environment:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies (if any):  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the main application:
```bash
python3 main.py
```

**Workflow:**
1. Enter your email and password (up to 3 attempts).  
2. View initial checking (\$4,321.00) and savings (\$6,543.21) balances.  
3. Choose an action:
   - `1` Deposit  
   - `2` Withdraw  
   - `3` Transfer  
   - `4` Check balances  
   - `q` Quit  
4. Follow on-screen prompts to complete the transaction.  

---

## Project Structure

```
.
├── BankingClasses/
│   ├── banking.py        # Abstract BankAccount base class
│   ├── checking.py      # CheckingAccount implementation
│   ├── savings.py       # SavingsAccount implementation
│   └── validation.py    # Email/password validators
├── BankingFunctions/
│   ├── deposit.py       # handle_deposit()
│   ├── withdraw.py      # handle_withdrawal()
│   └── transfer.py      # handle_transfer(), balances()
├── Assets/              # Mock-up terminal screenshots
│   ├── python-terminal-max-attempts.png
│   ├── python-terminal-options.png
│   └── ...
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
└── README.md            # You are here
```

---

## License

MIT © [Bryen Gatt]
