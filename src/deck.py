#Importing classes and modules required
import random 
#Importing Card class to create the deck
from src.card import Card

# creates the deck of 52 cards for the program
class Deck:

  #Initializing an empty deck of car4ds
  def __init__(self):
    self.cards = []
    
  #Generating the 52 cards for the deck
  def generate(self):
    #loops through all 13 cards a player can get 
      # 1 being an ace and 14 being a king
    for i in range(1, 14):
      #Loops through each type of suit
      for j in range(4):
        self.cards.append(Card(i, j))

  #Draw function that randomly selects cards from the deck and removes them 
  # which will then be returned as a list in order to be seen by user

  def draw(self, iteration):
    cards = []
    for i in range(iteration):
      card = random.choice(self.cards)
      #removes selected card from deck
      self.cards.remove(card)
      print(len(self.cards))
      #adds the randomly selected card to the card list
      cards.append(card)

    #The list of cards returned back to the user
    return cards

  #Count method used to count that the number of cards in the deck is 52 
  def count(self):
    return len(self.cards)

  