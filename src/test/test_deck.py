import unittest

try:
    from src.player import checkScore
except(ModuleNotFoundError, ImportError):
    from src.player import checkScore
from src.deck import generate
#from src.card import Card
from src.player import checkScore
#deck import Deck


class DeckTestCase(unittest.TestCase):

    def test_setUp(self):  # this method will be run before each test
        self.deck =  generate()
       

    def tearDown(self):  # this method will be run after each tests
        pass

   # def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        #number_of_cards = 0
        #self.deck = number_of_cards
        #self.assertEqual(number_of_cards, 52)

    #def test_deck_is_complete(self):
     #   test_deck = Deck.generate(self)
      #  self.assertEqual(test_deck.count(), 52)

    def test_check_score(self):
        assert checkScore(['A', 'A', '9'])== 21
        assert checkScore (['K', 'A']) == 21
        assert checkScore (['K', 'Q','A']) == 21




if __name__ == '__main__':
    unittest.main()
    print("")
