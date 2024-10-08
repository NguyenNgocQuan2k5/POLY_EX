import os
import sys

def clear_screen():
    print("Attempting to clear screen...")
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('clear')  # For Linux/macOS
    else:
        print("Unable to determine OS for screen clearing")
    print("")


clear_screen()

class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'
    
    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        else:
            self._transactions.append(amount)
            self.amount += amount

    def __add__(self, other):
        new_account = Account(f'{self.owner}&{other.owner}', self.amount + other.amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account

    def balance(self):
        return self.amount 
    
    def validate_transaction(self, amount_to_add):
        if self.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go below zero")
        else:
            self._transactions.append(amount_to_add)
            return f"New balance: {self.balance}"

if __name__ == "__main__":
    acc = Account('bob', 10)
    acc2 = Account('john')
    print(acc)
    print(repr(acc))
    acc.add_transaction(20)
    acc.add_transaction(-20)
    acc.add_transaction(30)
    print(acc.balance())
    print(len(acc._transactions))
    for transaction in acc._transactions:
        print(transaction)
    print(acc._transactions[1])
    print(list(reversed(acc._transactions)))
    acc2.add_transaction(10)
    acc2.add_transaction(60)
    print(acc.amount > acc2.amount)
    print(acc.amount >= acc2.amount)
    print(acc.amount < acc2.amount)
    print(acc.amount <= acc2.amount)
    print(acc.amount == acc2.amount)
    print(acc != acc2)
    acc3 = acc + acc2
    print(acc3)
    print(acc3._transactions)