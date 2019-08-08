# account.py

from BTrees.OOBTree import BTree
import persistent


class Accounts(BTree):
    pass


class Account(persistent.Persistent):

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def cash(self, amount):
        assert amount < self.balance
        self.balance -= amount
