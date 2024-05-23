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
        self.assertEqual(self.card.name, 'Alex')
        self.assertEqual(self.card.card_numbers, [])  
        print('Test 3.0 passed')

    def test_4(self):
        #Подготовка
        self.player1=loto.Player('Alex')
        self.player2=loto.Player('Alex')
        self.player3=loto.Player('ALex')
        
        self.barrel1=loto.Barrel()
        self.barrel2=loto.Barrel()

        self.card1=loto.Card('Alex')
        self.card2=loto.Card('ALex')

        #Тест
        self.assertEqual(str(self.player1), 'Alex')
        self.assertEqual(self.player1==self.player2, True)
        self.assertEqual(self.player1==self.player3, False)

        self.assertEqual(str(self.barrel1), 'Сейчас боченков: 90')
        self.assertEqual(self.barrel1==self.barrel2, True)
        self.barrel1.next_barrel()
        self.assertEqual(self.barrel1==self.barrel2, False)

        self.assertEqual(str(self.card1), 'Это карточка игрока: Alex')
        self.assertEqual(self.card1==self.card1, True)  #   !!!self.card1==self.card2!!!
        self.assertEqual(self.card1==self.card2, False)

        print('Test 4.0 passed')


    '''def setUp(self):
        # Подготовка к тестам, создание экземпляра игры и другие начальные действия
        self.new_game = loto.Game()
        self.test_player = loto.Player('Alex')
        self.new_game.list_players.append(self.test_player)
    def test_initial_state(self):
        # Тестирование начального состояния игры
        self.assertEqual(len(self.new_game.cards), 3)  # Проверяем количество карточек
        self.assertEqual(self.new_game.list_players[0].name, 'Alex')  # Проверяем количество карточек
        self.assertTrue(all(card.is_empty() for card in self.new_game.cards))  # Проверяем, что все карточки пусты
        self.assertTrue(all(card.is_empty() for card in self.new_game.cards))  # Проверяем, что все карточки пусты
    def test_gameplay(self):
        # # Тестирование игрового процесса
        self.game.start_game()  # Начинаем игру
        self.assertFalse(self.game.is_over())  # Проверяем, что игра не закончена после начала
        
        self.game.draw_number()  # Вытаскиваем номер
        self.assertEqual(len(self.game.drawn_numbers), 1)  # Проверяем, что был вытянут один номер
        
        self.game.check_cards()  # Проверяем карточки после вытягивания номера
        
         # Проверяем, что игра завершена после заполнения карточек
        while not self.game.is_over():
            self.game.draw_number()
            self.game.check_cards()
        self.assertTrue(self.game.is_over())'''

if __name__ == '__main__':
    unittest.main()
