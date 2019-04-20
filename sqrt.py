from fraction import Fraction

class SquareRoot(Fraction):
    # if we want to find out square root a of b
    # sqrt(a) = b; a = b^2
    # We select a starting number c.
    # And then we repeat c-= (c^2-b)/2c
    # many times, the number c will be very close to sqr(b),
    # which is the number a.

    def __init__(self, square, start):
        # we want to find out square root of this number
        self.square = square
        
        # we need a starting number which we will be adjusting on every iteration
        # if number is very big (over 10000000000), as a start, we use 100000,
        # else we use number close to the actual root. (see perfect_square.py)
        self.root = start

        # intermediate variables to recalculate the root
        self.root_squared = {"top": 0, "bottom": 0}
        self.factor_1 = {}
        self.factor_2 = {}
        self.root_change = {}


    def square_current_root(self):
        # square the c
        self.root_squared["top"] = self.root["top"]**2
        self.root_squared["bottom"] = self.root["bottom"]**2

    def calculate_factor_2(self):
        # calculate 2c
        self.factor_2 = self.multiply_fraction_by_value(self.root, 2)

    def calculate_factor_1(self):
        # calculate c^2 - b
        self.square_current_root()
        self.factor_1 = self.subtract_fractions(self.root_squared, self.square)

    def calculate_root_change(self):
        # calculate (c^2-b)/2c
        self.root_change = self.divide_fractions(self.factor_1, self.factor_2)

    def calculate_root(self):
        self.calculate_factor_1()
        self.calculate_factor_2()
        self.calculate_root_change()

        # subtract (c^2-b)/2c from c and simplify the fraction
        self.root = self.subtract_fractions(self.root, self.root_change)
        self.simplify_fraction(self.root)

    def return_root(self):
        return self.root

