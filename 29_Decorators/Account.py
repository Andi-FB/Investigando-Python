from timer_decorator import timer


class Account:
    """ An example class to hold an account data."""

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    @timer
    def deposit(self, balance):
        if balance > 0:
            self.balance += balance
        else:
            print('The balance should be greater than 0')

    @timer
    def withdraw(self, balance):
        if self.balance >= balance:
            self.balance -= balance
        else:
            print('Not enough funds')

    def get_balance(self):
        return self.balance

    def __str__(self):
        return 'Account number: {0}\nOwner: {1}\nBalance: {2}\n'.format(self.account_number, self.owner_name, self.balance)

