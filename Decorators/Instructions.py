from CurrentAccount import CurrentAccount
from InvestmentAccount import InvestmentAccount
from DepositAccount import DepositAccount

"""
The aim of this exercise its to develop your own decorator.
You will write a timer decorator to be used with methods in a class that take
the first parameter self, followed by one other parameter.
The decorator should log how long a method takes to execute.
To do this you can use the time module and import the default_timer.

from timeit import default_timer

You can then obtain a default_timer object for the start and end of a
function call and use these values to generate the time taken, for example:

start = default_timer()
func(self, value)
end = default_timer()
print('returned from ', func, 'it took', end - start,
'seconds')

You can then apply the decorator to the deposit() and withdraw()
methods defined in the Account class. For example,

@timer
def deposit(self, amount):
self._balance += amount
@timer
def withdraw(self, amount):
self._balance -= amount

These methods will be inherited by the DepositAccount and
InvestmentAccout classes. In the CurrentAccount class the withdraw
method is over written so you will also need to decorate that method with @timer
as well.
Now when you run your sample application you should get timing information
printed out for the deposit and withdraw methods:
calling deposit on Account[123] - John, current account =
10.05overdraft limit: -100.0 with 23.45
returned from deposit it took 8.009999999999268e-07 seconds
calling withdraw on Account[123] - John, current account =
33.5overdraft limit: -100.0 with 12.33
returned from withdraw it took 1.141999999999116e-06 seconds
"""
acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
acc2 = DepositAccount('345', 'John', 23.55, 0.5)
acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')
acc1.deposit(23.45)
acc1.withdraw(12.33)
acc1.withdraw(300.00)
acc2.deposit(23.45)
acc2.withdraw(12.33)
acc2.withdraw(300.00)
acc3.deposit(23.45)
acc3.withdraw(12.33)
acc3.withdraw(300.00)
print("FINISH")