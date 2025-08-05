class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f"Created account for {name} with ${balance}")
    
    def __str__(self):
        return f"Account: {self.name}, Balance: ${self.balance}"
    
    def __repr__(self):
        return f"BankAccount('{self.name}', {self.balance})"
    
    def __add__(self, other):
        # Combine two accounts
        new_balance = self.balance + other.balance
        return BankAccount(f"{self.name}+{other.name}", new_balance)
    
    def __eq__(self, other):
        # Compare accounts by balance
        return self.balance == other.balance
    
    def __lt__(self, other):
        # Compare accounts (less than)
        return self.balance < other.balance
    
    def __len__(self):
        # Return number of digits in balance
        return len(str(self.balance))

print("=== BANK ACCOUNT ===")
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)
account3 = BankAccount("Charlie", 1000)

print(f"Account 1: {account1}")
print(f"Account 2: {account2}")
print(f"Account 3: {account3}")

# Combining accounts
combined = account1 + account2
print(f"Combined account: {combined}")

# Comparing accounts
print(f"Alice and Charlie have same balance: {account1 == account3}")
print(f"Bob has less money than Alice: {account2 < account1}")

# Length of balance (number of digits)
print(f"Alice's balance has {len(account1)} digits")
print(f"Bob's balance has {len(account2)} digits")

