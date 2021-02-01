class BalanceError(Exception):

    def __init__(self, balance_value, account):
        self.balance_value = balance_value
        self.account = account

    def __str__(self):
        return 'Balance error you can not withdraw {0} from your Account, number: {1}. Have a good day {2}'.format(self.balance_value, self.account.account_number , self.account.owner_name)
