import unittest
import subprocess
from unittest.mock import patch
import sys
sys.path.insert(0, '../15')
import loto  # модуль с игрой в лото


class TestProgram(unittest.TestCase):
    def test_1(self):
        self.player = loto.Player('Alex')
        self.assertEqual(self.player.name, 'Alex')
        print("Test 1.0 passed")

    def test_2(self):
        self.barrel=loto.Barrel()
        self.assertEqual(self.barrel.left_barrels, 90)
        self.barrel.next_barrel()
        self.assertEqual(self.barrel.left_barrels, 89)
        print("Test 2.0 passed")

    def test_3(self):
        self.card=loto.Card('Alex')
        self.assertEqual(self.card.name,'Alex')
        self.assertEqual(self.card.card_numbers,[])  
        print('Test 3.0 passed')
