# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import re


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    st="Id: 67898176 jdh 787"
    # print(re.compile("Id: [0-9]{7}").search(st))
    print(bool(re.search("Id: [0-9]{7}",st)))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
