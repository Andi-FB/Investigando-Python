from Account import Account
from AmountError import AmountError
from BalanceError import BalanceError
"""
The InvestmentAccount will have a investment_type attribute which
can hold a string such as ‘safe’ or ‘high risk’.
"""


class InvestmentAccount(Account):
    @property
    def account_number(self):
        return self._account_number

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def balance(self):
        return self._balance

    def deposit(self, balance):
        if balance > 0:
            self._balance += balance
        else:
            raise AmountError(balance)

    def withdraw(self, balance):
        if self._balance >= balance:
            self._balance -= balance
        else:
            raise BalanceError(balance)

    def __init__(self, account_number, owner_name, balance, investment_type):
        super().__init__(account_number, owner_name, balance)
        self.investment_type = investment_type

    def __str__(self):
        return super().__str__() + 'Investment type: {}'.format(self.investment_type)
