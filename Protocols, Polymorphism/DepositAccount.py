from Account import Account
from AmountError import AmountError
from BalanceError import BalanceError


class DepositAccount(Account):

    def deposit(self, balance):
        print('in Deposit Account')
        if balance > 0:
            self._balance += balance
        else:
            raise AmountError(balance)

    def withdraw(self, balance):
        print('in Deposit Account')
        if self._balance >= balance:
            self._balance -= balance
        else:
            raise BalanceError(balance)

    def __init__(self, account_number, owner_name, balance, interest_rate):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + 'Interest rate: {}'.format(self.interest_rate)
