from Account import Account


class DepositAccount(Account):

    def __init__(self, account_number, owner_name, balance, interest_rate):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + 'Interest rate: {}'.format(self.interest_rate)
