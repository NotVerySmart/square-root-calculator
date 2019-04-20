from sqrt import SquareRoot
from sqrt_input_parser import Parser
from perfect_square import PerfectSquare

print("____________________________________________________________________")
print("_______________________Square root calculator_______________________")
print("____________________________________________________________________")
print("This program calculates the square root of the given number")
print("Separate numerator and denominator when inputing fractions with '/'")
print("For decimal numbers use ',' or '.'")


# endless loop so you don't need to restart program for every new number
while True:
    print("____________________________________________________________________")
    print("____________________________________________________________________")
    # input the string
    number_str = str(input("Input the number! "))
    print("\n")
    
    # convert the string to a fraction, if it
    parser = Parser(number_str)
    fraction = parser.parse()

    root_fraction = {}

    if type(fraction) == type("Invalid input"):
        # We get a string return only if the string is invalid
        # Print the error message
        print(fraction)

    else:
        # First check if the fraction is a prefect square of some other fraction
        perf_sqr = PerfectSquare(fraction)
        fraction_properties = perf_sqr.check()

        if fraction_properties["perfect-square"]:
            # If it is, we have finished
            root_fraction = fraction_properties["lower-border"]
        else:
            # If it isn't, we got an estimate of the root
            # to work with => to start the algorithm (if the number is small enough) 
            root = SquareRoot(fraction, fraction_properties["lower-border"])
            for i in range(25):
                root.calculate_root()

            root_fraction = root.return_root()

        # if the input string is valid, we can output the calculated root
        print("Square root of: {0} \ncan be written as: {1} / {2} \nwhich equals to: {3}"
            .format(
                number_str,
                root_fraction["top"],
                root_fraction["bottom"], 
                root_fraction["top"]/root_fraction["bottom"]
            )
        )



