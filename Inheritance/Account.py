class Account:
    """ An example class to hold an account data."""
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
        print('Instance count = {}'.format(cls.instance_count))

    def __init__(self, account_number, owner_name, balance):
        Account.increment_instance_count()
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, balance):
        if balance > 0:
            self.balance += balance
        else:
            print('The balance should be greater than 0')

    def withdraw(self, balance):
        if self.balance >= balance:
            self.balance -= balance
        else:
            print('Not enough funds')

    def get_balance(self):
        return self.balance

    def __str__(self):
        return 'Account number: {0}\nOwner: {1}\nBalance: {2}\n'.format(self.account_number, self.owner_name, self.balance)

