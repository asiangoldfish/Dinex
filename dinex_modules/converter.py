class Converter():
    """Container for various conversion between decimal, binary and hex values
    """

    def __init__(self):
        """Initialize vars that will be used by all functionalities
        """
        self.output = ""  # Stores the output in a variable that can be fetched externally or printed to terminal

    # Clear instanced output variable
    def __clear_output(self):
        """Clears the instanced output variable.

        Provides a simple way to clear the output, so the same variable can be used
        as an output to other methods should this class be used again.
        """
        self.output = ""

    # Prints the result of a completed calculation
    def results(self):
        """Provides a convinient way to print the result of a completed calculation
        """
        if self.output != "":
            print(self.output)

    # Handles converting decimal to binary values
    def dec_to_bin(self, user_input: str):
        """Converts decimal to binary values

        Capable of calculating a single decimal number or IPv4 and convert it to binary.
        Utilizes recursion, enabling an efficient method of calculation.

        Args:
            user_input (str): User input with of integers or an IPv4 address

        Returns:
            output (str): The output of the calculations
        """
        # Recursively converts decimal to binary value
        def conv(input: int, output: str = "") -> None:
            """Recursively converts decimal to binary values.

            To execute this conversion, the decimal value is always divided by 2 and converted to a whole number (to avoid floats).
            The remainder is always either 1 or 0 and is stored to the output variable, which can later be printed out or further manipulated.
            The result of the division is then used as the new user input and fed into this method again, creating a loop of conversion
            until the input is 1 and remainder is 0.

            In summary, the steps of the calculation happens as follows: Take an integer number and divide it by two. Convert it to the lowest
            whole number. Note the remainder, and run this process again until the quotient is 0 and remainder is 1.

            Args:
                output (str): Variable to store the output digits in
                input (int): Integer number to convert to binary digits with

            Returns:
                str: Returns the output of the calculation or recursively re-runs the method again
            """

            # If the input is 0, then we dividing it by 2 will just result in 0. Therefore we stop the calculation here and return the output
            if input == 0:
                return output

            else:
                # Step 1: Take a number and divide it by 2, rounding the product to the lowest whole number
                new_input = input//2

                # Step 2: Find the remainder of the division
                remainder = input - (new_input * 2)

                # Step 3: Calculation is complete if the remainder is 0 and quotient is 1
                if remainder == 0 and input == 1:
                    return output
                # Step 3: If not, then...
                else:
                    # note the remainder and
                    output = str(remainder) + output
                    # rerun the process again.
                    return conv(new_input, output)

        # Clear output before adding binary digits to it
        self.__clear_output()

        # No point in converting if the user is trying to convert 0 to binary... It just equals to 0
        if user_input == "0":
            self.output = user_input
            return

        # Enables converting to binary even if user input is an IPv4 formatted address.
        # Only checks for for "."
        user_input = user_input.split(".")

        # Execute calculation

        for i, octet in enumerate(user_input):
            # Skip the octet if it's only an empty string
            if octet == "":
                continue

            # The octet must be an integer. We return an error message to user if it isn't an integer
            try:
                octet = int(octet)
            except ValueError:
                # Change the output alltogether and return an error message to the user
                self.output = "Only integers and periods are accepted"
                return

            # Add newly calculated octet to the output returned back to user
            self.output += conv(octet)

            # Add "." to the IPv4 address if it isn't the last iteration
            if i < len(user_input) - 1:
                self.output += "."
