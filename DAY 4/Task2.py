class BankAccount:
    # Parameterized constructor
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("Bank account created successfully.")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}")
            print("Updated Balance:", self.balance)
        else:
            print("Invalid deposit amount.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
            print("Updated Balance:", self.balance)

    # Destructor
    def __del__(self):
        print(f"Bank account {self.account_number} is being closed.")


# Create BankAccount object
account1 = BankAccount(123456, 5000)

# Perform operations
account1.deposit(2000)
account1.withdraw(3000)
account1.withdraw(6000)  # Invalid withdrawal

# Delete object explicitly
del account1
