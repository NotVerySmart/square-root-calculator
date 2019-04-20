

class Parser:
    # convert the string into a fraction if it is valid
    # else return why it is invalid
    def __init__(self, input_string):
        self.input_string = input_string

        self.valid_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", ",", "."]
        
        # To diferentiate why string is invalid (to many separating chars or invalid char)
        # Imediately when a invalid char is detected, error message is returned
        # If too many separating chars are used, 
        # the error is returned after iterating over all chars.
        self.is_valid = True 

        self.separating_chars = [",", ".", "/"]
        self.separating_char = ""

        self.string_parts = []

        self.fraction = {"top": 0, "bottom": 0}

    def validate_and_guess_type(self):
        # Go over every character and make sure it is valid.
        # Also check if the char is among separating chars.
        for char in self.input_string:
            if char not in self.valid_chars:
                # Character not valid
                self.is_valid = False
                return False

            if char in self.separating_chars and self.separating_char == "":
                # First separating char in the string, note which one it is
                self.separating_char = char
            elif char in self.separating_chars and self.separating_char != "":
                # More than one separating char, meaning the string is invalid
                self.is_valid = False
        return True

    def separate_string(self):
        if self.separating_char != "":
            self.string_parts = self.input_string.split(self.separating_char)

    def create_fraction(self):
        # Make a fraction out of the string according to the separating char
        if self.separating_char == "/":
            self.fraction["top"] = int(self.string_parts[0])
            self.fraction["bottom"] = int(self.string_parts[1])
        elif self.separating_char in [",", "."]:
            top = int(self.string_parts[0] + self.string_parts[1])
            bottom = int(top / float(self.string_parts[0] + "." + self.string_parts[1]))
            self.fraction["top"] = top
            self.fraction["bottom"] = bottom
        else:
            self.fraction["top"] = int(self.input_string)
            self.fraction["bottom"] = 1

    def parse(self):
        if self.validate_and_guess_type():
            if self.is_valid:
                self.separate_string()
                self.create_fraction()
                return self.fraction
            else:
                return 'Too many separating characters (",", ".", "/"), only one can be used!'
        else:
            return 'Invalid characters, use only "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", ",", "."'