# Generator for C++ Projects
import os

def main():
    print("==============================\nProgen - C++ Project Generator v0.0.1")
    print("Copyright (C) 2015 Sean Francis N. Ballais")
    projName = input("Project Name: ")
    projChoice = input("Should we convert the directory name ({0}) to lowercase? (Y/N) ".format(projName))
    projChoice = projChoice.lower()

    if (projChoice == 'y'):
        projName = projName.lower()
        print("Converted the directory name to lowercase...")

    print("Using {0} as project directory...".format(projName))

    # Create the project folder then set up the folders inside the project folder
    if (os.path.exists(projName)):
        print("Unable to create the project folder. Folder already present.")
        projChoice = input("Use the existing folder (will delete its contents)? (Y/N) ")
        projChoice = projChoice.lower()

        if (projChoice == 'n'):
            print("Folder cannot be used. Exiting...")
            return

        os.removedirs(projName)

    print("\nDefault folders: [{0}, bin, build, include, src, lib]".format(projName))
    # Enter other folders to include
    arbitraryFolders = input("Other folders to include (separate folders using commas): ")
    folders = [
        projName,
        "bin",
        "build",
        "include",
        "src",
        "lib"
    ]

    if (arbitraryFolders != ""):
        folders = folders.extend(arbitraryFolders.split(','))

    for folder in folders:
        os.makedirs(folder)
        print("Created the {0} folder...".format(folder))

        if (folder == projName):
            os.chdir(folder)

    print("Finished generating the project folders of {0}...".format(projName))