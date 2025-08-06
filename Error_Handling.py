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

# Example 2

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter only numbers.")
finally:
    print("This block always executes.")