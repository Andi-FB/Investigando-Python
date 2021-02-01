from CurrentAccount import CurrentAccount
from DepositAccount import DepositAccount
from InvestmentAccount import InvestmentAccount

"""
The aim of this exercise is to use an Abstract Base Class.
The Account class of the project you have been working on throughout the last
few chapters is currently a concrete class and is indeed instantiated in our test
application.
Modify the Account class so that it is an Abstract Base Class which will force
all concrete examples to be a subclass of Account.
"""
acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
print(acc1)
acc2 = DepositAccount('345', 'John', 23.55, 0.5)
acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'risky')
print(acc2)
print(acc3)
