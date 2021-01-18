class Transaction:

    def __init__(self, t_type, amount):
        self._t_type = t_type
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @property
    def t_type(self):
        return self._t_type

    def __str__(self):
        return "Transaction({0}: {1})".format(self.t_type, self.amount)


