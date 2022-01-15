from unittest import TestCase

from character import *


class Test(TestCase):
    def testReadFileSurvivors(self):
        """
        Test for the read of survivors
        """
        displayList(survivors)
        print(len(survivors))

    def testReadFileHunters(self):
        """
        Test for the read of hunters
        """
        displayList(hunters)
        print(len(hunters))

    def testRandomSurvivor(self):
        """
        Test for the random choice of the survivor
        """
        chosenSurvivor = randomChoice(survivors)
        print("The chosen survivor is : " + chosenSurvivor)

    def testRandomHunter(self):
        """
        Test for the random choice of the hunter
        """
        chosenHunter = randomChoice(hunters)
        print("The chosen hunter is : " + chosenHunter)

    def testRandomTrait(self):
        """
        Test for the random choice of the trait
        """
        chosenTrait = randomChoice(traits)
        print("The chosen trait is : " + chosenTrait)
