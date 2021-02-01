from Account import Account
"""
The InvestmentAccount will have a investment_type attribute which
can hold a string such as ‘safe’ or ‘high risk’.
"""


class InvestmentAccount(Account):
    def __init__(self, account_number, owner_name, balance, investment_type):
        super().__init__(account_number, owner_name, balance)
        self.investment_type = investment_type

    def __str__(self):
        return super().__str__() + 'Investment type: {}'.format(self.investment_type)
