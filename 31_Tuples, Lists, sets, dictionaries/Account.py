from Transaction import Transaction


class Account:
    """ An example class to hold an account data."""

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self._transactions = []
        init = Transaction('Deposit', balance)
        self._transactions.append(init)

    def deposit(self, balance):
        if balance > 0:
            self.balance += balance
            transaction = Transaction('Deposit', balance)
            self._transactions.append(transaction)
        else:
            print('The balance should be greater than 0')

    def withdraw(self, balance):
        if self.balance >= balance:
            self.balance -= balance
            transaction = Transaction('Withdraw', balance)
            self._transactions.append(transaction)
        else:
            print('Not enough funds')

    def get_balance(self):
        return self.balance

    def __str__(self):
        return 'Account number: {0}\nOwner: {1}\nBalance: {2}\n'.format(self.account_number, self.owner_name, self.balance)

    def __iter__(self):
        return iter(self._transactions)

    def __next__(self):
        return next(self._transactions)