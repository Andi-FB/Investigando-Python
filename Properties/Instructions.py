from CurrentAccount import CurrentAccount
from InvestmentAccount import InvestmentAccount
from DepositAccount import DepositAccount
from Account import Account

"""
In this exercise you will add properties to an existing class.
Return to the Account class that you created several chapters ago; convert the
balance into a read only property using decorators, then verify that the following
program functions correctly:

"""
acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
acc2 = DepositAccount('345', 'John', 23.55, 0.5)
acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')
#Trying out the setter property
acc1.account_number = 'FOO BAR'
print(acc1)
print(acc2)
print(acc3)
acc1.deposit(23.45)
acc1.withdraw(12.33)
print('balance:', acc1.balance)
print('Number of Account instances created:', Account.instance_count)
print('balance:', acc1.balance)
acc1.withdraw(300.00)
print('balance:', acc1.balance)
#This line should not change the balance as it propery is defined only for the getter and stop program execution.
acc1.balance = 2123
