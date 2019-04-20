

class Fraction:
    # class providing basic numeric operations on fractions
    # reduce, multiply by value, divide with a fraction, 
    # subtract, make 2 fractions have the same denominator

    def greatest_common_divisor(self, a, b):
        # največji skupni delitelj
        while True:
            r = a % b
            if (r == 0):
                return b
            a = b
            b = r

    def lowest_common_multiple(self, a, b):
        gcd = self.greatest_common_divisor(a, b)
        return int((a * b) / gcd)

    def simplify_fraction(self, fraction):
        gcd = self.greatest_common_divisor(fraction["top"], fraction["bottom"])
        # we modify the original dictionary (not creating a new one)
        fraction["top"] = int(fraction["top"]/gcd)
        fraction["bottom"] = int(fraction["bottom"]/gcd)

    def multiply_fraction_by_value(self, frac, value):
        # the original dictionary should not be altered (new one is created)
        fraction = {"top": frac["top"] * value, "bottom": frac["bottom"]}
        self.simplify_fraction(fraction)
        return fraction

    def fractions_to_same_bottom(self, f1, f2): #tested
        new_bottom = self.lowest_common_multiple(f1["bottom"], f2["bottom"])

        # the original dictionaries should not be altered (new are created)
        fraction1 = {"top": f1["top"] * new_bottom / f1["bottom"], "bottom": new_bottom}
        fraction2 = {"top": f2["top"] * new_bottom / f2["bottom"], "bottom": new_bottom}

        return fraction1, fraction2

    def subtract_fractions(self, f1, f2):
        # from fraction 1 subtract fraction 2
        fraction1, fraction2 = self.fractions_to_same_bottom(f1, f2)

        # subtract
        fraction1["top"] -= fraction2["top"]
        self.simplify_fraction(fraction1)
        return fraction1

    def divide_fractions(self, f1, f2):
        # multiply fraction 1 with inverse value of fraction 2
        bottom = f1["bottom"] * f2["top"]
        top = f1["top"] * f2["bottom"]
        fraction = {"top": top, "bottom": bottom}

        self.simplify_fraction(fraction)
        return fraction