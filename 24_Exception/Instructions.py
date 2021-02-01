from CurrentAccount import CurrentAccount
from AmountError import AmountError
from BalanceError import BalanceError

"""
This exercise involves adding error handling support to the CurrentAccount class.
In the CurrentAccount class it should not be possible to withdraw or deposit
a negative amount.
Define an exception/error class called AmountError. The AmountError
should take the account involved and an error message as parameters.
Next update the deposit() and withdraw() methods on the Account and
CurrentAccount class to raise an AmountError if the amount supplied is negative.
You should be able to test this using:
try:
acc1.deposit(-1)
except AmountError as e:
print(e)

This should result in the exception 'e' being printed out, for example:
Next modify the class such that if an attempt is made to withdraw money which
will take the balance below the over draft limit threshold an Error is raised.
AmountError (Cannot deposit negative amounts) on Account[123] -
John, current account = 21.17overdraft limit: -100.0

The Error should be a BalanceError that you define yourself. The
BalanceError exception should hold information on the account that generated
the error.
Test your code by creating instances of CurrentAccount and taking the
balance below the overdraft limit.
Write code that will use try and except blocks to catch the exception you
have defined.
You should be able to add the following to your test application:
try:
print('balance:', acc1.balance)
acc1.withdraw(300.00)
print('balance:', acc1.balance)
except BalanceError as e:
print('Handling Exception')
print(e)

"""
acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
try:
    acc1.deposit(-1)
except AmountError as e:
    print(e)

try:
    print('balance:', acc1.balance)
    acc1.withdraw(300.00)
    print('balance:', acc1.balance)
except BalanceError as e:
    print('Handling Exception')
    print(e)
