from Account import Account
from BalanceError import BalanceError
"""
The CurrentAccount class can have an overdraft_limit attribute. This
can be set when an instance of a class is created and altered during the lifetime of
the object. The overdraft limit should be included in the __str__() method used
to convert the account into a string.
The CurrentAccount withdraw() method should verify that the balance
never goes below the overdraft limit. If it does then the withdraw() method
should not reduce the balance instead it should print out a warning message.
"""


class CurrentAccount(Account):

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
