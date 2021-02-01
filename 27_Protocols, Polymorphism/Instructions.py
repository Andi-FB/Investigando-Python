from CurrentAccount import CurrentAccount

"""
The aim of this exercise is to use an Abstract Base Class.
The Account class of the project you have been working on throughout the last
few chapters is currently a concrete class and is indeed instantiated in our test
application.
Modify the Account class so that it is an Abstract Base Class which will force
all concrete examples to be a subclass of Account.
"""

with CurrentAccount('891', 'Adam', 5.0, 50.0) as acc:
    acc.deposit(23.0)
    acc.withdraw(12.33)
    print(acc.balance)
