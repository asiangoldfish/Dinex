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
                int(octet)
            except ValueError:
                # Change the output alltogether and return an error message to the user
                self.output = "Only integers and periods are accepted"
                return

            # Add newly calculated octet to the output returned back to user
            # If there's only 0's in the octet, then just return the octet
            if set(octet) == {"0"}:
                self.output += octet
            else:
                self.output += conv(int(octet))

            # Add "." to the IPv4 address if it isn't the last iteration
            if i < len(user_input) - 1:
                self.output += "."

    # Handles converting binary to decimal values
    def bin_to_dec(self, args: str):
        """Handles the logic for converting binary to decimal

        The binary is converted to decimal by checking the length of the input and
        using the length as the exponent to 2. Effectively, it's 2**n-i, where i is
        the index of iteration while looping through each binary digit.
        """

        # Recursive calculation from binary to decimal
        def conv(input_binary: str, segment_length: int, temporary_output: int = 0) -> int:
            """Recursively convert binary digits to decimal values

            We use recursion so we can efficiently perform the calculations. We start with the
            most significant bit and go through each bit at a time. Parameter segment_length
            therefore also becomes the index of the index we're currently working on.

            Steps of calculation:
            1. Find the first digit of the input segment.
            2. If the binary digit is 1, calculate 2**n (segment length) and add that to temporary_output
            3. If it is 0, then iterate to the next digit
            4. Recursively repeat this process until n == 1

            Args:
                input_binary (str): Input segment of binary digits to convert to decimal
                segment_length (int): This value is there so we know what the most
                                        significant bit is and its value in decimal.
                temporary_output (int): Temporarily stores the output of the conversion.
                                        This parameter is used only for the recursion and
                                        should not be passed when called.

            Returns:
                temporary_output(int): The decimal values calculated by the method
            """
            # Step 1: Find the first digit and identify if it's 0 or 1.
            # Return if there's no more digits to calculate. Will otherwise throw an index error.
            try:
                first_digit = input_binary[0]
            except IndexError:
                return temporary_output

            # Step 3: Binary digit is 0, hence go to next iteration
            if first_digit == "0":
                return conv(input_binary[1:], segment_length-1, temporary_output)

            # Step 2: Digit is 1, hence calculate 2**n
            pow_two_to_n = 2**segment_len
            temporary_output += pow_two_to_n

            # Step 4: Recursively repeat the process until n == 1
            if segment_len == 1:
                return temporary_output
            else:
                return conv(input_binary[1:], segment_length-1, temporary_output)

        self.__clear_output()

        # Check that there's only 1's, 0's or .'s in the user input
        for i in set(args):
            if i not in ["1", "0", "."]:
                self.output = "Only 0, 1 and . are valid inputs"
                return

        # The formula is 2**n-i, where n is the total length of each segment of the
        # input and i is the iteration looping through each digit.
        # We split args by ".", because the input could be related to network addresses
        segmented_args = args.split(".")

        for i, segment in enumerate(segmented_args):
            # We need this to know the value of the most significant bit
            segment_len = len(segment)
            # Add the result of the calculation to the output var of the instance
            self.output += str(conv(input_binary=segment,
                                    segment_length=segment_len-1))

            # Assume that we're dealing with network addresses if user argument contains
            # two or more segments. Therefore, add a period after each segment
            if i < len(segmented_args) - 1:
                self.output += "."
