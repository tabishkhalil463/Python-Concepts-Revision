def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance for withdrawal.")
    return balance - amount

try:
    current_balance = 1000
    withdrawal_amount = int(input("Enter amount to withdraw: "))
    remaining = withdraw(current_balance, withdrawal_amount)
    print("Withdrawal successful. Remaining balance:", remaining)
except ValueError as e:
    print("Error:", e)