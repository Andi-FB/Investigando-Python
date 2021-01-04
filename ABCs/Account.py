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
    @abstractmethod
    def account_number(self):
        pass

    @account_number.setter
    @abstractmethod
    def account_number(self, acc_number):
        pass

    @property
    @abstractmethod
    def owner_name(self):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass

    @abstractmethod
    def deposit(self, balance):
        pass

    @abstractmethod
    def withdraw(self, balance):
        pass

    def __str__(self):
        return 'Account number: {0}\nOwner: {1}\nBalance: {2}\n'.format(self.account_number, self.owner_name,
                                                                        self.balance)
