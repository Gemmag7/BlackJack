import unittest
from src.card import Card
import src.player as player
import src.deck as Deck
from src.deck import Deck 


class DeckTestCase(unittest.TestCase):

    def test_setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    #def test_number_of_cards(self): 
         # any method beginning with 'test' will be run by unittest
        #number_of_cards = len(self.deck.cards)
        #self.assertEqual(number_of_cards, 52)

#This test will determine if the scores are calculated correctly 
#This method also checks the Ace rule to ensure that if a user's score is already 11 or above and their hand already has an ace, then the value of the second ace will be set to 1 instead of 11
    def test_check_score(self):
        check_score = player.Player.test_check_score
        test_card1 =['A', 'A', '9']
        test_card2 =['K', 'A']
        test_card3 = ['K', 'Q', 'A']
        test_card4 = ['K', 'A', 'Q']
        #src.Player.checkScore
        self.assertEqual(check_score(test_card1),21)
        self.assertEqual(check_score(test_card2),21)
        self.assertEqual(check_score(test_card3),21)
        #Difference between test_card 3 & 4 is the order of the Ace card
        #3 will pass since total is 20 before Ace is calculated, making the value of the ace 1 
        #4 will not pass due to the total of the hand being 10 before Ace card, making the value of the ace 11
        self.assertEqual(check_score(test_card4), 21)


if __name__ == '__main__':
    unittest.main()
