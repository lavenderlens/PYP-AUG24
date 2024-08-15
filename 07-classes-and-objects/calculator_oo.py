class Calculator:
    # our previously global variable total
    # becomes a prop of the Calculator object
    # we declare it in the __init__
    def __init__(self):
        self.total = 0 # the same as the global var

    def add(self, num):
        self.total += num

    def sub(self, num):
        self.total -= num

    def mul(self, num):
        self.total *= num

    def div(self, num):
        self.total /= num

    def equals(self):
        return_value = self.total
        self.total = 0
        return return_value