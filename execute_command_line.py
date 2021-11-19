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

    # Command for converting decimal to binary values
    parser.add_argument("-db", "--DecimalToBinary", metavar="", type=str,
                        help="Enter integers or an IPv4 address")

    # Verbose and quiet functionalities. They are mutually exclusive
    vq_group = parser.add_mutually_exclusive_group()
    vq_group.add_argument("-q", "--quiet", action="store_true",
                          help="Print quiet")
    vq_group.add_argument("-v", "--verbose", action="store_true",
                          help="Print verbose")

    # Store user input in a variable
    args = parser.parse_args()

    # Logic for decimal to binary conversion
    if args.DecimalToBinary is not None:
        # Import module here, otherwise the logic in conv is executed automatically
        from dinex_modules import Converter

        con = Converter()
        con.dec_to_bin(args.DecimalToBinary)
        con.results()
