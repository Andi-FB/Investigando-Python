from AmountError import AmountError


class Account:
    """ An example class to hold an account data."""
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
        print('Instance count = {}'.format(cls.instance_count))

    def __init__(self, account_number, owner_name, balance):
        Account.increment_instance_count()
        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = balance

    # Added the account_number property just to write a setter too
    @property
    def account_number(self):
        """Docstring here.... This is the docstring for the account_number property"""
        return self._account_number

    @account_number.setter
    def account_number(self, acc_number):
        if isinstance(acc_number, str):
            self._account_number = acc_number

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def balance(self):
        """This is the docstring for the balance property"""
        return self._balance

    def deposit(self, balance):
        if balance > 0:
            self._balance += balance
        else:
            raise AmountError(balance)

    def withdraw(self, balance):
        if self.balance >= balance:
            self.balance -= balance
        else:
            print('Not enough funds')

    def __str__(self):
        return 'Account number: {0}\nOwner: {1}\nBalance: {2}\n'.format(self.account_number, self.owner_name,
                                                                        self.balance)
