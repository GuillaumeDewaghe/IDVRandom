from unittest import TestCase

from characters import *


class Test(TestCase):
    def testReadFileSurvivors(self):
        """
        Test for the read of survivors
        """
        survivors = readFile("Survivors.txt")
        displayList(survivors)

    def testReadFileHunters(self):
        """
        Test for the read of hunters
        """
        hunters = readFile("Hunters.txt")
        displayList(hunters)

    def testRandomSurvivor(self):
        """
        Test for the random choice of the survivor
        """
        survivors = readFile("Survivors.txt")
        chosenSurvivor = randomChoice(survivors)
        print("The chosen survivor is : " + chosenSurvivor)

    def testRandomHunter(self):
        """
        Test for the random choice of the hunter
        """
        hunters = readFile("Hunters.txt")
        chosenHunter = randomChoice(hunters)
        print("The chosen hunter is : " + chosenHunter)

    def testRandomTrait(self):
        """
        Test for the random choice of the trait
        """
        traits = ["Listen", "Abnormal", "Excitment", "Patroller", "Teleport", "Peeper", "Blink"]
        chosenTrait = randomChoice(traits)
        print("The chosen trait is : " + chosenTrait)
