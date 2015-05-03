# Progen class
# License under the GPL v3.0
# Copyright (C) 2015 Sean Francis N. Ballais
from .engine import Progen
import os
import sys

def main():
    # Run engine
    prg = Progen()
    if len(sys.argv) == 2:
        arg = sys.argv[1]
    else:
        arg = ""

    # Command line arguments
    # -h or --help for usage help
    # -l or --list for listing the generators
    # -v or --version for listing the version
    if arg == "" or arg == "-h" or arg == "--help":
        if arg == "":
            print("Command or option not specified.")
        prg.usageHelp()
    elif arg == "-l" or arg == "--list":
        prg.listGenerators()
    elif arg == "-v" or arg == "--version":
        prg.version()
    elif arg != "-h" or arg != "--help" or arg != "-l" or arg != "--list" or arg != "-v" or arg != "--version":
        prg.runGenerator(arg)
    exit()