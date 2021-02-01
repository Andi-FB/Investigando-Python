from CurrentAccount import CurrentAccount
from InvestmentAccount import InvestmentAccount
from DepositAccount import DepositAccount

"""
The aim of this exercise is to work with a collection/container such as a list.
To do this we will return to your Account related classes.
You should modify your Account class such that it is able to keep a history of
transactions.
A Transaction is a record of a deposit or withdrawal along with an amount.
Note that the initial amount in an account can be treated as an initial deposit.
The history could be implemented as a list containing an ordered sequence to
transactions. A Transaction itself could be defined by a class with an action (deposit
or withdrawal) and an amount.
Each time a withdrawal or a deposit is made a new transaction record should be
added to a transaction history list.
Now provide support for iterating through the transaction history of the account
such that each deposit or withdrawal can be reviewed. You can do this by implementing the Iterable protocol—refer to the last chapter if you need to check how to
do this. Note that it is the transaction history that we want to be able to iterate
through—so you can use the history list as the basis of your iterable.
You should be able to run this following code at the end of your Accounts
application:

for transaction in acc1:
 print(transaction)
 
Depending upon the exact set of transactions you have performed (deposits and
withdrawals) you should get a list of those transactions being printed out:
Transaction[deposit: 10.05]
Transaction[deposit: 23.45]
Transaction[withdraw: 12.33]

"""
acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
acc1.deposit(203)
acc1.withdraw(12)
acc1.withdraw(121)
acc1.deposit(1)
for trans in acc1:
 print(trans)