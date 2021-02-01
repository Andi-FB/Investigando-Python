from Account import Account
from AmountError import AmountError
from BalanceError import BalanceError
"""
The InvestmentAccount will have a investment_type attribute which
can hold a string such as ‘safe’ or ‘high risk’.
"""


class InvestmentAccount(Account):

    def deposit(self, balance):
        print('in Investment Account')
        if balance > 0:
            self._balance += balance
        else:
            raise AmountError(balance)

    def withdraw(self, balance):
        print('in Investment Account')
        if self._balance >= balance:
            self._balance -= balance
        else:
            raise BalanceError(balance)

    def __init__(self, account_number, owner_name, balance, investment_type):
        super().__init__(account_number, owner_name, balance)
        self.investment_type = investment_type

    def __str__(self):
        return super().__str__() + 'Investment type: {}'.format(self.investment_type)
