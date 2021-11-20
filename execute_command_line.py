from typing import List
import argparse
import sys


# Execute command given by user (called by the dinex utility command)
def execute_command_line(argv: List[str] = ...):
    # Create a parser object
    parser = argparse.ArgumentParser(description="Square a number")

    # Print help msg if no arguments were given
    if len(sys.argv) == 1:
        print("Missing commands. type dinex -h for help")
        exit()

    # Command for converting decimal to binary values
    parser.add_argument("-db", "--decimal-to-binary", metavar="", type=str,
                        help="convert decimal to binary values")
    parser.add_argument("-bd", "--binary-to-decimal", metavar="",
                        type=str, help="convert binary to decimal values")

    # Verbose and quiet functionalities. They are mutually exclusive
    vq_group = parser.add_mutually_exclusive_group()
    vq_group.add_argument("-q", "--quiet", action="store_true",
                          help="Print quiet")
    vq_group.add_argument("-v", "--verbose", action="store_true",
                          help="Print verbose")

    # Store user input in a variable
    args = parser.parse_args()

    # Import dinex modules only after everything is setup and ready. This is for
    # performance optimization
    from dinex_modules import Converter

    con = Converter()

    # Logic for decimal to binary conversion
    if args.decimal_to_binary is not None:
        # Import module here, otherwise the logic in conv is executed automatically

        con.dec_to_bin(args.decimal_to_binary)
        con.results()

    # Logic for binary to decimal conversion
    if args.binary_to_decimal is not None:
        con.bin_to_dec(args.binary_to_decimal)
        con.results()
