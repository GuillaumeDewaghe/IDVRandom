from unittest import TestCase

from main import readFile


class Test(TestCase):
    def testReadFileSurvivors(self):
        """

        :return:
        """
        survivors = readFile("Survivors.txt")
        for survivor in survivors:
            print(survivor)

    def testReadFileHunters(self):
        hunters = readFile("Hunters.txt")
        for hunter in hunters:
            print(hunter)