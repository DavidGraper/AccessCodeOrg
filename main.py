import glob
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def getfiles(pathtosearch):
    searchstring = pathtosearch + "*.txt"

    files = glob.glob(searchstring)

    return files

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    files2read = getfiles("u:\\Academic Schedule DB\\Access Programming\\")

    lines = []

    for file in files2read:

        print(file)

        with open(file) as f:
            lines = f.readlines()

            x = []
            for line in lines:
                x = re.match(r"(Private |Public )*(Function|Sub)( \w*)(.*)", line)

                if x:
                    # print(line)
                    print(x.groups())





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
