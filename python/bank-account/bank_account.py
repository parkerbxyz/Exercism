from threading import Lock

from dataclasses import dataclass


@dataclass
class BankAccount:
    active: bool = False
    balance: int = None
    lock: object = Lock()

    def get_balance(self):
        with self.lock:
            if not self.active:
                raise ValueError("Cannot get balance of closed account.")
            return self.balance

    def open(self):
        if self.active:
            raise ValueError("Account is already open.")
        self.active = True
        self.balance = 0

    def deposit(self, amount):
        with self.lock:
            self._check_transaction(amount)
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            self._check_transaction(amount)
            if amount > self.balance:
                raise ValueError("NSF: Cannot withdraw more than deposited.")
            self.balance -= amount

    def close(self):
        if not self.active:
            raise ValueError("Account already closed.")
        self.balance = None
        self.active = False

    def _check_transaction(self, amount):
        if not self.active:
            raise ValueError("Cannot perform transactions on closed accounts.")
        if amount < 0:
            raise ValueError("Transaction amount must be greater than zero.")
