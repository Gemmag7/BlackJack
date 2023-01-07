#Card class used to create each card in the deck 
class Card: 
  def __init__(self, value, suit):

    #The score value of the card i.e. King = 10, Ace = 1 or 11
    self.score = value
    #The face of the card i.e. Ace, King, 4, etc. 
    self.face = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
    
    #The suit of the card that has icons represented for each suit
    self.suit = '♠♣♥♦'[suit]

  #This module shows the card each player has formatted as a playing card
  def show(self):
    print('┌───────┐')
    print(f'| {self.face:<2}    |')
    print('|       |')
    print(f'|   {self.suit}   |')
    print('|       |')
    print(f'|    {self.face:>2} |')
    print('└───────┘')  

  #Value getter function that will return the value of each card.
  #Each card is usually set a numeric value to match its suit except .. cards that have to use this method to have a numeric value assigned. 
  def value(self):
    #If the face of the card is a Jack, King or Queen then the value of the card will be set to 10
    if self.score >= 10:
      return 10
    #If the face of the card is an Ace, then the value of the card will be 11 
    elif self.score == 1:
      return 11
    return self.score


###FOR LATER DEVELOPMENT#####
#When the program is ran, dealer cards aren't displayed because of loop. In a later stage of development, I hope to fix this bug so that one card will display for dealer and one remains hidden##
  def hideCard(self):
    print('┌───────┐')
    print('|       |')
    print('|       |')
    print('| ????? |')
    print('|       |')
    print('|       |')
    print('└───────┘') 
