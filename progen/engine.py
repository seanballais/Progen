# Progen class
# License under the GPL v3.0
# Copyright (C) 2015 Sean Francis N. Ballais
from os import listdir
from os.path import isfile, join
from .version import __version__
import os

class Progen:
    def usageHelp(self):
        print("usage: progen [--version] [--help] [--list] [generator]")
        print("\t-v or --version\tDisplays the version number of Progen")
        print("\t-h or --help\tDisplays this help")
        print("\t-l or --list\tLists the available project generators")
        print("\tgenerator\tAny of the generators available")

    def listGenerators(self):
        print("List of available generators:")
        
        gen_path = os.path.dirname(os.path.abspath(__file__)) + "/generators"

        generators = [gen for gen in listdir(gen_path) if isfile(join(gen_path, gen))]

        for gen in generators:
            if gen != "__init__.py":
                print("- {0}\n".format(gen[:-3]))

    def runGenerator(self, generator):
        try:
            gen = __import__("generators.%s" % generator, fromlist=["progen.generators"])
        except ImportError:
            print("Generator ({0}) not found".format(generator))
            exit()

        if hasattr(gen, "folders"): # Folders must be a list
            for folder in gen.folders:
                os.makedirs(folder)
            print("Finished creating the project files...")
        else:
            gen.main()

    def version(self):
        print("Progen version: {0}".format(__version__))