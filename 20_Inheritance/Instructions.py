from CurrentAccount import CurrentAccount
from InvestmentAccount import InvestmentAccount
from DepositAccount import DepositAccount

"""
The aim of these exercises is to extend the Account class you have been developing from the last two chapters
by providing DepositAccount, CurrentAccount and InvestmentAccount subclasses.
Each of the classes should extend the Account class by:
• CurrentAccount adding an overdraft limit as well as redefining the withdraw method.
• DepositAccount by adding an interest rate.
• InvestmentAccount by adding an investment type attribute.
These features are discussed below:
The CurrentAccount class can have an overdraft_limit attribute. This
can be set when an instance of a class is created and altered during the lifetime of
the object. The overdraft limit should be included in the __str__() method used
to convert the account into a string.
The CurrentAccount withdraw() method should verify that the balance
never goes below the overdraft limit. If it does then the withdraw() method
should not reduce the balance instead it should print out a warning message.
The DepositAccount should have an interest rate associated with it which is
included when the account is converted to a string.
The InvestmentAccount will have a investment_type attribute which
can hold a string such as ‘safe’ or ‘high risk’.
This also means that it is no longer necessary to pass the type of account as a
parameter—it is implicit in the type of class being created.
"""
# CurrentAccount(account_number, account_holder,
# opening_balance, overdraft_limit)
acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
print(acc1)
# DepositAccount(account_number, account_holder,opening_balance,
# interest_rate)
acc2 = DepositAccount('345', 'John', 23.55, 0.5)
print(acc2)
# InvestmentAccount(account_number, account_holder, opening_balance,
# investment_type)
acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')
print(acc3)
acc1.deposit(23.45)
acc1.withdraw(12.33)
print('balance:', acc1.get_balance())
acc1.withdraw(300.00)
print('balance:', acc1.get_balance())
