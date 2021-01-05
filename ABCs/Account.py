from abc import ABCMeta, abstractmethod


class Account(metaclass=ABCMeta):
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
        return self._account_number

    @account_number.setter
    def account_number(self, acc_number):
        self._account_number = acc_number

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def deposit(self, balance):
        pass

    @abstractmethod
    def withdraw(self, balance):
        pass

    def __str__(self):
        return 'Account number: {0}\nOwner: {1}\nBalance: {2}\n'.format(self.account_number, self.owner_name,
                                                                        self.balance)
