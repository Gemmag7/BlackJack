#Importing the deck module in order for each player to be dealt cards
from src.deck import Deck
from src.card import Card
from unittest import TestCase

#Player class is used to handle the interactions that the user may choose such as hit or deal.
class Player:

  #__innit__ method used to create default values for the class
  #cards is set to an empty list, default score is set to 0 
  #deck is the deck that has been generated for the game
  #isDealer is used to identify if the user is a player and not the dealer
  def __init__(self, isDealer, deck):
    self.cards =[]
    self.isDealer =  isDealer
    self.deck = deck
    self.score = 0

  #Method is responsible for user obtaining a new card and adding this card to their hand
  #The score will be updated when the new card is added to the hand
  def hit(self):
    #extend method is used to call the draw method in the deck class and then add the newly selected card to the current list of cards
    self.cards.extend(self.deck.draw(1))
    #The checkScore method is used to calculate the new score after the new card has been added to the hand
    self.checkScore()
    #if score is greater than 21 then the player/dealer's hand should lose
    if self.score > 21:
      return 1
    #0 will be returned to the blackjack.py class and the corresponding message will display to the user
    return 0

  #Deal method is used to deal cards to the player and dealer
  def deal(self):
    #extend method is used to call the draw method in the deck class and then add the newly selected card to the current list of cards
    self.cards.extend(self.deck.draw(2))
     #The checkScore method is used to calculate the new score after the new card has been added to the hand
    self.checkScore()
    #if player's score is equal than 21 then they win the round of blackjack 
    if self.score == 21:
      return 1
    return 0

  #CheckScore method 
  def checkScore(self):
    #Setting the default value of the aceCounter to 0 whilst no ace cards have been drawn from the deck 
    aceCounter = 0 
    #Setting the default value of score to 0 before checking the score of all cards in the hand
    self.score = 0
    
    #looping through each card in the hand
    for card in self.cards:
      #Checking to see if the card in each hand is an ace
      if card.value ==11:
        #ace counter increments if a card with value 11 is found
        aceCounter += 1
        if self.cards.__contains__(aceCounter ==2):
          #sets the value of the ace card to 1 if there is already an ace card in the player's hand
          card.value ==1
      #the score is updated with the new value of the ace card if there is already an ace card and the score of the card is equal to or greater than 11.
      self.score += card.value()

    #while there are at least 2 aces in the hand and the score of the hand is greater than or equal to 11, the score of the hand will be reduced by 10 so that the value of an ace card will be reduced to 1 instead of 11
    while aceCounter >=2 and self.score >=11:
      aceCounter -=1
      self.score -=10
    #Score is returned 
    return self.score

  #showCards method is called to display each user's cards 
  def showCards(self):
    if self.isDealer:
      print("Dealer's Cards: ")
    else:
      print("Player's Cards: ")
    
    #For loop used to loop through each player's cards to show them
    for i in self.cards:
      #Calls the show method in card.py
      i.show()

    #each player's score is calculated and then shown 
    print("Score: "  +str(self.score))


#ONLY FOR TESTING PURPOSES 
  
  def test_check_score(testCards):
    #localised version of the card faces and their values will be used here for testing
    faces = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
    total = 0
    for card in testCards:
      #checks to see if the card is an Ace card and also checks if the total is greater than or equal to 11
      #if total >= 11, then the value of the ace card is set to 1 
      #if total >11, then the ace card remains with value 11
      if card == 'A' and total >= 11:
        total +=1
      else:     
        total += faces[card]
    return total