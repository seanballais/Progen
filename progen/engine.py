# Progen class
# License under the GPL v3.0
# Copyright (C) 2015 Sean Francis N. Ballais
import version

class Progen:
    def main(arg):
        # Command line arguments
        # -h or --help for usage help
        # -l or --list for listing the generators
        # -v or --version for listing the version
        if arg == "-h" or arg == "--help":
            self.usageHelp()
        elif arg == "-l" or arg == "--list":
            self.listGenerators()
        elif arg == "-v" or arg == "--version":
            self.version()
        elif arg != "" and 
             arg != "-h" or arg != "--help" or
             arg != "-l" or arg != "--list" or
             arg != "-v" or arg != "--version":
            self.runGenerator()
        else:
            print("Unknown option or command\n")

    def usageHelp(self):
        print("usage: progen [--version] [--help] [--list] [generator]\n")
        print("\n\n")
        print("\t-v or --version\tDisplays the version number of Progen\n")
        print("\t-h or --help\tDisplays this help")
        print("\t-l or --list\tLists the available project generators\n")
        print("\tgenerator\tAny of the generators available\n")

    def listGenerators(self):
        pass

    def runGenerator(self):
        pass

    def version(self):
        print("Progen version: {0}\n".format(version.__version__))