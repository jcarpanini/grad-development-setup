# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:42:46 2024

@author: carpa
"""

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        """Initialize the bank account with the account holder's name and initial balance."""
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds are available."""
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}.")

    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance


def main():
    # Get the account holder's name and initial balance
    name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance (default is $0): ") or 0)

    # Create a bank account instance
    account = BankAccount(name, initial_balance)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current balance: ${account.get_balance():.2f}")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()

#Francely Collaboration on this File
Print('hello')
