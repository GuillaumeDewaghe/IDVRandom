import random

from typing import List


def readFile(fileName: str):
    """
    Function which allows to read a file and to save the content.

    :param str fileName: Name of the file we want to read
    :return: List of survivors or hunters
    :rtype: list[str]
    """
    with open("../texts/" + fileName + "", "r") as file:
        lines = file.read().splitlines()
    return lines


def displayList(itemsList: List[str]):
    """
    Displays all the elements from the list

    :param list[str] itemsList: List of survivors, hunters or traits
    """
    for item in itemsList:
        print(item)


def randomChoice(itemsList: List[str]):
    """
    Shuffles and chooses a random element from the list

    :param list[str] itemsList: List of survivors, hunters or traits
    :return: A element from the list
    :rtype: str
    """
    # print("----- Before shuffle -----\n")
    # displayList(itemsList)
    random.shuffle(itemsList)
    # print("\n----- After shuffle -----\n")
    # displayList(itemsList)
    chosen = random.choice(itemsList)
    return chosen

# TODO: Create a function to input the survivors and the hunters we have
