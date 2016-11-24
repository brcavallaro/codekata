# Bruno Cavallaro
# Date: 11, November, 2016

import re
import rules

class Checkout(object):

    def __init__(self):
        """
        Initialize the object Checkout with an empty cart.
        :return none
        """
        self.cart = {}

    def scan(self, codes):
        """
        Scan the string with the product sequence and store it in the cart.
        :return none
        """
        for code in codes:
            if code in self.cart:
                self.cart[code] += 1
            else:
                self.cart[code] = 1

    def calculate_total(self):
        """
        Calculate the total amount considering the items from cart.
        :return total: int
        """
        total = 0

        # Iterate through the dictionary that has the product
        # codes and their occurences (how many times they appeared
        # in the string scanned).
        for code, occurence in self.cart.iteritems():
            counter = {}
            product = code * occurence
            prices_rules = list(reversed(sorted(rules.prices[code].keys())))

            # Iterate through prices rules and search how many times
            # the product appears in the sequence of the rule, then calculate
            # the totals. It does it recursively with the "rest" until the
            # prices rules list is finished.
            for rule in prices_rules:
                counter[rule] = 0
                ls = re.findall('.{1,' + str(rule) + '}', product)
                for item in ls:
                    if len(item) != rule:
                        product = item
                    else:
                        product = ""
                        counter[rule] += 1

            # Calculate the total amount throught the iteration
            # of the dictionary from file rules.py.
            for group, value in counter.iteritems():
                total += rules.prices[code][group] * value

        return total


if __name__ == '__main__':
    pass
