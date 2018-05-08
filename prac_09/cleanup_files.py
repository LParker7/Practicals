"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('.')
    # print a list of all files (test)
    # print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')


    for dir_name, subdir_list, file_list in os.walk('Lyrics'):
        # print(os.listdir('.'))
        # print(os.getcwd())
        # loop through each file in the (original) directory
        for filename in file_list:
            # ignore directories, just process files
            if not os.path.isdir(filename):
                new_name = get_fixed_filename(filename)
                print(new_name)

                # NOTE: These options won't just work...
                # they show you ways of renaming and moving files,
                # but you need to have valid filenames. You can't make a file with
                # a blank name, and on Windows you can't have files with the same
                # characters but different case (e.g. a.TXT and A.txt)
                # So, you need to get valid filenames before you can use these.

                # Option 1: rename file to new name - in place
                if filename != new_name:
                    os.rename("{}/".format(dir_name) + filename, "{}/".format(dir_name) + new_name)

                # Option 2: move file to new place, with new name
                # shutil.move("{}/".format(dir_name) + filename, "{}/".format(dir_name) + new_name)

                # Processing subdirectories using os.walk()

                # os.chdir('..')  # .. means "up" one directory
                # for dir_name, subdir_list, file_list in os.walk('Lyrics'):
                #     print("In", dir_name)
                #     print("\tcontains subdirectories:", subdir_list)
                #     print("\tand files:", file_list)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")

    new_name = ""
    for i, character in enumerate(filename):
        if i != 0 and filename[i - 1].isalpha() and filename[i].isupper():
            new_name += "_{}".format(character)
        elif i != 0 and filename[i - 1] == '_' and filename[i].islower():
            new_name += "{}".format(character.upper())
        else:
            new_name += character
    new_name = new_name[0].upper() + new_name[1:]
    return new_name


main()
