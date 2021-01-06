from Account import Account
from BalanceError import BalanceError
from AmountError import AmountError


class CurrentAccount(Account):

    def deposit(self, balance):
        if balance > 0:
            self._balance += balance
        else:
            raise AmountError(balance)

    def __init__(self, account_number, owner_name, balance, overdraft_limit):
        super().__init__(account_number, owner_name, balance)
        self._overdraft_limit = overdraft_limit

    def __str__(self):
        return super().__str__() + 'Overdraft: {}'.format(self.overdraft_limit)

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, new_limit):
        self._overdraft_limit = new_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit < amount:
            raise BalanceError(amount, self)
        else:
            self._balance -= amount
