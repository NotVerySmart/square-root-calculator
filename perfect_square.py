from fraction import Fraction

class PerfectSquare(Fraction):
    def __init__(self, fraction):
        self.fraction = fraction
        self.simplify_fraction(self.fraction)
        
        self.top = self.fraction["top"]
        self.top_lower_border = False
        
        self.bottom = self.fraction["bottom"]
        self.bottom_lower_border = False


    def iterate(self):
        if self.top >= 10000000000 or self.bottom >= 10000000000:
            # The numbers are too big, the while loop would take too long.
            # Skip this part and take some number to make the program faster
            # but less accurate.
            self.top_lower_border = 100000
            self.bottom_lower_border = 1
        else:
            i = 1
            square = 1
            # Try to figure out if fraction's numerator and denominator
            # are squares of whole numbers.
            # If they are not, figure out between which two whole numbers
            # square root of numerator and denominator are.
            # Then use the lower number to further calculate the root.
            while ((not self.top_lower_border) or (not self.bottom_lower_border)):
                square = i**2
                if self.top <= square and not self.top_lower_border:
                    self.top_lower_border = i
                
                if self.bottom <= square and not self.bottom_lower_border:
                    self.bottom_lower_border = i

                i += 1

    def check(self):
        self.iterate()
        
        if (self.top == self.top_lower_border**2 and self.bottom == self.bottom_lower_border**2):
            is_perfect_square = True
            # If both numerator and denominator are squares of whole numbers
            # then we have discovered the root of the fraction. 
        
        else:
            is_perfect_square = False
            # If they are not, pass forward the two numbers between
            # square roots of numerator and denominator are.
            # 3/17  => root of 3 is between 1 and 2; return 1 {lower number}
            #       => root of 17 is between 4 and 5; return 4
            # for sqrt(3/17) return 1/4 to further calculate the root

        return {
            "perfect-square": is_perfect_square,
            "lower-border": {
                "top": self.top_lower_border,
                "bottom": self.bottom_lower_border
            }
        }