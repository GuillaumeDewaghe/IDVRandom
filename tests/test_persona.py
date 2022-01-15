from unittest import TestCase

from classes.persona import Persona
from classes.persona import survivorsPersonaWeb
from classes.persona import huntersPersonaWeb
from classes.persona import isAllPersonaCoordinatesDifferent
from classes.persona import displayPersonaWeb
from classes.persona import randomPersonaWeb


class TestPersona(TestCase):
    def testShowInfo(self):
        persona1 = Persona("Distress", 1, 0, 1)
        persona2 = Persona("Curiosity", 1, 1, 0)
        persona1.showInfo()
        persona2.showInfo()
        listPersona = [persona1, persona2]
        print(len(listPersona))
        for persona in listPersona:
            print(persona.showInfo())

    def testSurvivorsPersonaWeb(self):
        index = 0
        for persona in survivorsPersonaWeb:
            print(f"i = {index} :")
            print(f"{persona.showInfo()}")
            index += 1
        if len(survivorsPersonaWeb) == 32:
            print("All the survivors personas are here !")
        else:
            print("Some survivors personas are missing !")

    def testHuntersPersonaWeb(self):
        index = 0
        for persona in huntersPersonaWeb:
            print(f"i = {index}, {persona.showInfo()}")
            index += 1
        if len(huntersPersonaWeb) == 32:
            print("All the hunters personas are here !")
        else:
            print("Some hunters personas are missing !")

    def testIsAllSurvivorsCoordinatesDifferent(self):
        print(isAllPersonaCoordinatesDifferent(survivorsPersonaWeb))

    def testIsAllHuntersCoordinatesDifferent(self):
        print(isAllPersonaCoordinatesDifferent(huntersPersonaWeb))

    def testDisplayPersonaWeb(self):
        # index = 0
        # for persona in survivorsPersonaWeb:
        #     print(f"i = {index} :")
        #     print(f"{persona.showInfo()}")
        #     index += 1
        displayPersonaWeb(survivorsPersonaWeb)

    def testRandomPersonaWeb(self):
        count = 0
        randomSurvivorPersonaWeb = randomPersonaWeb(survivorsPersonaWeb)
        for persona in randomSurvivorPersonaWeb:
            count += persona.value * 5
        print(f"Number of points used : {count}")
        displayPersonaWeb(randomSurvivorPersonaWeb)
