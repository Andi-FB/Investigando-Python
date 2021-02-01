from abc import ABCMeta, abstractmethod

"""
This exercises focuses on attribute look up.
You should add a method to the Account class that can be used to handle how
accounts should behave when an attempt is made to access an undefined attribute.
In this case you should log the attempt to access the attribute (which means print
out a warning message) then return a default value of −1.
For example, if you had the following line to your application:
print('acc1.branch:', acc1.branch)
Then this should invoke the __getattr__() method for the undefined
attribute branch. Print a warning message and then return the value −1 which will
be printed by the above statement.
The output of this statement should be something like:
__getattr__: unknown attribute accessed - branch
acc1.branch: -1 

####
Monkey patching is done to extend the object / Class functionality 
Account.name = 'All the Accounts will have this name if no override is done'
acc1.name = 'Acc 1 name'

This is related on how python performs the method lookup. First it starts at instance level and goes higher through class, parent class...
####
"""


class Account():
    """ An example class to hold an account data."""

    def __enter__(self):
        print('Entered: {}'.format(self.owner_name))
# Here is usually done the database connection, for example
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exited: {}'.format(self.owner_name))
# Here is usually done the database connection close, for example
        return True

    def __getattr__(self, item):
        print('__getattr__: ', item)
        print('item not found returning default value')
        return -1

    def __init__(self, account_number, owner_name, balance):
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

    def deposit(self, balance):
        if balance > 0:
            self._balance += balance
        else:
            print('Error tryng to deposit')

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit < amount:
            print('Error withdrawing money')
        else:
            self._balance -= amount

    def __str__(self):
        return 'Account number: {0}\nOwner: {1}\nBalance: {2}\n'.format(self.account_number, self.owner_name,
                                                                        self.balance)


acc1 = Account('123', 'Pepe', 200)
print('acc1.branch:', acc1.branch)