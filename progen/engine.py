# Progen class
# License under the GPL v3.0
# Copyright (C) 2015 Sean Francis N. Ballais

class Progen:
    def main(arg):
        # Command line arguments
        # -h or --help for usage help
        # -l or --list for listing the generators
        if arg == "-h" or arg == "--help":
            self.usageHelp()
        elif arg == "-l" or arg == "--list":
            self.listGenerators()
        else:
            self.runGenerator()

        pass

    def usageHelp(self):
        pass

    def listGenerators(self):
        pass

    def runGenerator(self):
        pass