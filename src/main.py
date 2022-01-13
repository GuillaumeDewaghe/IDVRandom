
def readFile(fileName):
    """
    Function which allows to read a file and to save the content.

    :param string fileName: Name of the file we want to read
    :return: List of survivors or hunters
    :rtype: list[str]
    """
    with open("../texts/" + fileName + "", "r") as file:
        lines = file.readlines()
    return lines


def printPersonaWeb():
    """
    Function which displays the persona web of the random survivor or hunter.
    """
    print('------')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# survivors = readFile("Survivors.txt")
# hunters = readFile("Hunters.txt")
# survivorsT = tuple(survivors)
# for survivor in survivorsT:
#     print(survivor)
# printPersonaWeb()
# for hunter in hunters:
#     print(hunter)
# print(len(hunters))
