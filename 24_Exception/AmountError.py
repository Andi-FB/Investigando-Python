class AmountError(Exception):
    """Amount deposited must be greater than zero"""
    def __init__(self, deposit_value):
        self.deposit_value = deposit_value

    def __str__(self):
        return "Amount Error Exception, Amount = {0}. Must be greater than zero".format(self.deposit_value)
