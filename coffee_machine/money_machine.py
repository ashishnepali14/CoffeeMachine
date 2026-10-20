class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    # this is a very specific thing, but you should model this in ints (numbers of pennies), not floats
    # the reason being is that floats are not perfectly accurate in computers.
    # see (https://docs.python.org/3/tutorial/floatingpoint.html)
    # At the scale of this program it doesn't matter, however in large scale transactions
    # it really does! You can still print things as floats afterwards.
    # limitation of this is that there are limits on int sizes 
    # https://www.datacamp.com/tutorial/everything-you-need-to-know-about-pythons-maximum-integer-value

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            # this is vulnerable to entering empty strings, you may want to catch it and force a retry
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
