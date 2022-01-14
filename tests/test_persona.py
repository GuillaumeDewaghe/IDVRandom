from unittest import TestCase

from classes.persona import Persona
from classes.persona import survivorsPersonaWeb


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
        personaWeb = survivorsPersonaWeb
        for persona in personaWeb:
            print(persona.showInfo())
        if len(personaWeb) == 32:
            print("All the survivors personas are here !")
        else:
            print("Some survivors personas are missing !")

