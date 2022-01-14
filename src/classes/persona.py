import random

from typing import List


class Persona:

    def __init__(self, name, maximum, x, y):
        """
        Constructor of the class Persona

        :param str name: Name of the persona
        :param int maximum: Maximum of the persona
        :param int x: Coordinate x of the persona
        :param int y: Coordinate y of the persona
        """
        self.name = name
        self.value = 0
        self.maximum = maximum
        self.x = x
        self.y = y

    def showInfo(self):
        """
        Show all the information about the persona
        """
        print(f"Name = {self.name}, value = {self.value}, maximum = {self.maximum}, x = {self.x}, y = {self.y}")

    def incrementValue(self):
        if self.value < self.maximum:
            self.value = self.value + 1


def isAllPersonaCoordinatesDifferent(personaWeb: List[Persona]):
    """
    Function to verify if all the coordinates of the personas are different or not.

    :param list[Persona] personaWeb: Persona web of a survivor or a hunter
    :return: True if all the coordinates are different, else false
    """
    for persona in personaWeb:
        for persona2 in personaWeb:
            # print(f"persona = {persona.showInfo()}, persona2 = {persona2.showInfo()}")
            # print("----------------------------------------------------------------------")
            if persona.name != persona2.name:
                if persona.x == persona2.x and persona.y == persona2.y:
                    print(f"{persona.name} and {persona2.name} have the same x and y !")
                    return False
    return True


def displayPersonaWeb(personaWeb: List[Persona]):
    # North branch
    print(f"\t" * 10 + f"{personaWeb[3].value}")
    print(f"\t" * 10 + "|")
    print(f"\t" * 8 + f"   {personaWeb[6].value}    {personaWeb[2].value}")
    print(f"\t" * 9 + "\   |")
    print(
        f"\t" * 8 + f"{personaWeb[5].value} -- {personaWeb[4].value}  {personaWeb[1].value}  {personaWeb[7].value}     {personaWeb[13].value}")
    print(f"\t" * 9 + "  \ | /     /")
    print(
        f"\t" * 8 + f" {personaWeb[31].value}      {personaWeb[0].value}      {personaWeb[12].value} -- {personaWeb[14].value}")
    print(f"\t" * 8 + "  \     |     /")

    # West and East branches
    print(f"\t" * 5
          + f"{personaWeb[27].value} -- {personaWeb[26].value} -- {personaWeb[25].value} -- {personaWeb[24].value} -- "
          + "*"
          + f" -- {personaWeb[8].value} -- {personaWeb[9].value} -- {personaWeb[10].value} -- {personaWeb[11].value}")

    # South Branch
    print(f"\t" * 8 + "  /     |     \ ")
    print(
        f"\t" * 7 + f"{personaWeb[30].value} -- {personaWeb[28].value}      {personaWeb[16].value}      {personaWeb[15].value}")
    print(f"\t" * 8 + "/     / | \ ")
    print(
        f"\t" * 7 + f"   {personaWeb[29].value}     {personaWeb[23].value}  {personaWeb[17].value}  {personaWeb[20].value} -- {personaWeb[21].value}")
    print(f"\t" * 10 + "|   \ ")
    print(f"\t" * 10 + f"{personaWeb[18].value}    {personaWeb[22].value}")
    print(f"\t" * 10 + "|")
    print(f"\t" * 10 + f"{personaWeb[19].value}")


# TODO: Create a function which gives a random persona
def randomPersona():
    
    random.randint(1, 16)


survivorsPersonaWeb = \
    [
        # North branch
        Persona("Distress", 1, 0, 1),
        Persona("Sticker", 3, 0, 2),
        Persona("Symbiotic Effect", 3, 0, 3),
        Persona("Spectator", 1, 0, 4),

        Persona("Survivor's Instinct", 1, -1, 2),
        Persona("Healing", 3, -2, 3),
        Persona("Air Walk", 3, -1, 3),
        Persona("Obsessive", 1, 1, 2),

        # East branch
        Persona("Curiosity", 1, 1, 0),
        Persona("Escape", 3, 2, 0),
        Persona("Compensate", 3, 3, 0),
        Persona("Borrowed Time", 1, 4, 0),

        Persona("Distraction", 1, 2, 1),
        Persona("Snooze", 3, 3, 2),
        Persona("Self Deception", 3, 3, 1),
        Persona("Cold", 1, 2, -1),

        # South branch
        Persona("Drawbridge Effect", 1, 0, -1),
        Persona("Savior Complex", 3, 0, -2),
        Persona("Herd Mentality", 3, 0, -3),
        Persona("Tide Turner", 1, 0, -4),

        Persona("Sneak", 1, 1, -2),
        Persona("Doctor", 3, 2, -3),
        Persona("Shelter", 3, 1, -3),
        Persona("Mech Elite", 1, -1, -2),

        # West branch
        Persona("Risky Move", 1, -1, 0),
        Persona("Horsefly Effect", 3, -2, 0),
        Persona("Knee Jerk Reflex", 3, -3, 0),
        Persona("Broken Windows", 1, -4, 0),

        Persona("Prisoner's Dilemma", 1, -2, -1),
        Persona("Great Power", 3, -3, -2),
        Persona("Will to Survive", 3, -3, -1),
        Persona("Exit Path", 1, -2, 1)
    ]

huntersPersonaWeb = \
    [
        # North branch
        Persona("Deteriorate", 1, 0, 1),
        Persona("Wither", 3, 0, 2),
        Persona("Destructiveness", 3, 0, 3),
        Persona("Confined Space", 1, 0, 4),

        Persona("Panic", 1, -1, 2),
        Persona("Rage", 3, -2, 3),
        Persona("Berserker", 3, -1, 3),
        Persona("Restraint", 1, 1, 2),

        # East branch
        Persona("Owl", 1, 1, 0),
        Persona("Hunter's Instinct", 3, 2, 0),
        Persona("Hospitable", 3, 3, 0),
        Persona("Trump Card", 1, 4, 0),

        Persona("Announcement", 1, 2, 1),
        Persona("Wanted Order", 3, 3, 2),
        Persona("Impact", 3, 3, 1),
        Persona("Desperate Fight", 1, 2, -1),

        # South branch
        Persona("Inertia", 1, 0, -1),
        Persona("Mock", 3, 0, -2),
        Persona("Carnival", 3, 0, -3),
        Persona("Detention", 1, 0, -4),

        Persona("Quenching Effect", 1, 1, -2),
        Persona("Control Freak", 3, 2, -3),
        Persona("Giant Claw", 3, 1, -3),
        Persona("No Survivors", 1, -1, -2),

        # West branch
        Persona("Deer Hunt", 1, -1, 0),
        Persona("Possessive", 3, -2, 0),
        Persona("After Effects", 3, -3, 0),
        Persona("Insolence", 1, -4, 0),

        Persona("Tinnitus", 1, -2, -1),
        Persona("Hunt", 3, -3, -2),
        Persona("Street Sweeper", 3, -3, -1),
        Persona("Claustrophobia", 1, -2, 1)
    ]
