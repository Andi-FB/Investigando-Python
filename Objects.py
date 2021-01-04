"""
The aim of this exercise is to create a new class called Account.
1. Define a new class to represent a type of bank account.
2. When the class is instantiated you should provide the account number, the name
of the account holder, an opening balance and the type of account (which can be
a string representing 'current', 'deposit' or 'investment' etc.). This means that
there must be an __init__ method and you will need to store the data within
the object.
3. Provide three instance methods for the Account; deposit(amount),
withdraw(amount) and get_balance(). The behaviour of these
methods should be as expected, deposit will increase the balance, withdraw will
decrease the balance and get_balance() returns the current balance.
4. Define a simple test application to verify the behaviour of your Account class.
"""


class Account:
    """ An example class to hold an account data."""
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
        print('Instance count = {}'.format(cls.instance_count))

    def __init__(self, account_number, owner_name, balance, type_of_account):
        Account.increment_instance_count()
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.type_of_account = type_of_account

    def deposit(self, balance):
        if balance > 0:
            self.balance += balance
        else:
            print('The balance should be greater than 0')

    def withdraw(self, balance):
        if self.balance >= balance:
            self.balance -= balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return 'Account number: {0}\nOwner: {1}\nBalance: {2}\nType of account: {3}\n'.format(self.account_number, self.owner_name, self.balance, self.type_of_account)


acc1 = Account('123', 'John', 10.05, 'current')
acc2 = Account('345', 'John', 23.55, 'savings')
acc3 = Account('567', 'Phoebe', 12.45, 'investment')
print(acc1)
print(acc2)
print(acc3)
acc1.deposit(23.45)
acc1.withdraw(12.33)
print('balance:', acc1.get_balance())
print('Number of Account instances created:', Account.instance_count)

"""
The aim of this exercise is to add housekeeping style methods to the Account class.
You should follow these steps:
1. We want to allow the Account class from the last chapter to keep track of the
number of instances of the class that have been created.
2. Print out a message each time a new instance of the Account class is created.
3. Print out the number of accounts created at the end of the previous test program.
For example add the following two statements to the end of the program:
print('Number of Account instances created:',
Account.instance_count)

#Added in the code above this comment.
"""
