import random


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
        print(f"Name = {self.name}, value = {self.value}, maximum = {self.maximum}, x = {self.x}, y = {self.y}")

    # TODO: Create a function to display the persona web
    def displayPersonaWeb(self):
        for x in range(-4, 4):
            for j in range(-4, 4):
                pass

    def incrementValue(self):
        if self.value < self.maximum:
            self.value = self.value + 1

    # TODO: Create a function which gives a random persona
    def randomPersona(self):
        random.randint(1, 16)


# TODO: Create lists of survivors and hunters persona web
survivorsPersonaWeb = \
    [
        # North persona
        Persona("Distress", 1, 0, 1),
        Persona("Sticker", 3, 0, 2),
        Persona("Symbiotic Effect", 3, 0, 3),
        Persona("Spectator", 1, 0, 4),

        Persona("Survivor's Instinct", 1, -1, 2),
        Persona("Healing", 3, -2, 3),
        Persona("Air Walk", 3, -1, 3),
        Persona("Obsessive", 1, 1, 2),

        # East persona
        Persona("Curiosity", 1, 1, 0),
        Persona("Escape", 3, 2, 0),
        Persona("Compensate", 3, 3, 0),
        Persona("Borrowed Time", 1, 4, 0),

        Persona("Distraction", 1, 2, 1),
        Persona("Snooze", 3, 3, 2),
        Persona("Self Deception", 3, 3, 1),
        Persona("Cold", 1, 2, -1),

        # South persona
        Persona("Drawbridge Effect", 1, 0, -1),
        Persona("Savior Complex", 3, 0, -2),
        Persona("Herd Mentality", 3, 0, -3),
        Persona("Tide Turner", 1, 0, -4),

        Persona("Sneak", 1, 1, -2),
        Persona("Doctor", 3, 2, -3),
        Persona("Shelter", 3, 1, -3),
        Persona("Mech Elite", 1, -1, -2),

        # West persona
        Persona("Risky Move", 1, -1, 0),
        Persona("Horsefly Effect", 3, -2, 0),
        Persona("Knee Jerk Reflex", 3, -3, 0),
        Persona("Broken Windows", 1, -4, 0),

        Persona("Prisoner's Dilemma", 1, -2, 1),
        Persona("Great Power", 3, -3, -2),
        Persona("Will to Survive", 3, -3, -1),
        Persona("Exit Path", 1, -2, 1)
    ]
