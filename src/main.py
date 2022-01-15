import os
from typing import List

from character import survivors, hunters, randomChoice, traits
from classes.persona import survivorsPersonaWeb, huntersPersonaWeb, randomPersonaWeb, displayPersonaWeb, Persona


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def menu():
    print("-" * 100 + "\n"
          + "-" * 38 + " RANDOMIZER IDENTITY V " + "-" * 39 + "\n"
          + "-" * 100 + "\n"
          + "This program will gives you a random survivor or hunter with a random persona web and trait (if hunter).\n")


def main():
    ok = False
    while not ok:
        menu()
        choice = input("Do you want a random survivor or hunter ?\n"
                       + "1 - Survivor\n"
                       + "2 - Hunter\n"
                       + "3 - I changed my mind, I want to exit the randomizer\n"
                       + "choice = ")
        choice = int(choice)
        match choice:
            case 1:
                clearConsole()
                ok = True
                # print("Survivor")
                chosenSurvivor = randomChoice(survivors)
                randomSurvivorPersonaWeb = randomPersonaWeb(survivorsPersonaWeb)
                print(f"Random survivor : {chosenSurvivor} \n"
                      f"Random survivor's persona web : \n")
                displayPersonaWeb(randomSurvivorPersonaWeb)
            case 2:
                clearConsole()
                ok = True
                # print("Hunter")
                chosenHunter = randomChoice(hunters)
                chosenTrait = randomChoice(traits)
                randomHunterPersonaWeb = randomPersonaWeb(huntersPersonaWeb)
                print(f"Random hunter : {chosenHunter} \n"
                      f"Random trait : {chosenTrait} \n"
                      f"Random hunter's persona web : \n")
                displayPersonaWeb(randomHunterPersonaWeb)
            case 3:
                clearConsole()
                ok = True
                print("Bye have a great time !")
            case _:
                print("Wrong choice, choose a correct one !")
                i = input("Press Enter to continue...")
                clearConsole()
    print("End of the program")


if __name__ == '__main__':
    main()
