#Importing modules needed for game
from src.deck import Deck
from src.player import Player

#The main class of the program. The application will be ran using "python blackjack.py". 
#The
class blackjack:
  def __init__(self) -> None:
    self.deck = Deck()
    #generates a deck for the game
    self.deck.generate()
    #Assigns the player a deck as well as setting the isDealer variable to false in order to have player status
    self.player = Player(False, self.deck)
    #Assigns the dealer a deck as well as setting the isDealer variable to true in order to have dealer status
    self.dealer = Player(True, self.deck)

  #The play method is in charge of starting the round of blackjack
  def play(self):

    #This isn't needed. Was used to ensure that 52 cards are in a deck
    #print("Number of cards in deck: " + str(self.deck.count()))

    #player is dealt their hand 
    player_hand = self.player.deal()

    #dealer is dealt their hand
    dealer_hand = self.dealer.deal()

    #Showing the player's cards 
    self.player.showCards()

    #from the player class, binary response is returned back to the blackjack class. 
    #If 1 is sent back, then the player/dealer has reached blackjack
    #If 0 is sent back, then the player/dealer has not reached blackjack
    if player_hand == 1:
      #if the player's hand is returned 1, then a message will display stating that they have won
      print("Player wins! Congrats!")
      if dealer_hand ==1:
        #If the dealer's hand is returned 1, then a message will display stating that  both player and dealer have won
        print("Dealer and Player both win! It's a push!")
      return 1 

    #Setting command as an empty string
    command = ""

    #loop carried out whilst command is not changed to string value of "S". 
    while command != "S":
      #bust is set to false binary value since user still has to decide whether to hit or stand
      bust = 0
      #command string that uses user input to gather if user wishes to stand or hit
      #Program accepts capital H for Hit and capital S for stand 
      command = input("[H]it or [S]tand?")

      #If user inputs a capital H, then they will be dealt with another card to their hand.
      if command =="H":
        #hit method is called in the player class 
        bust = self.player.hit()
        #Player's hand is shown including the new card dealt as well as an updated score
        self.player.showCards()

      #If bust reaches true, then a message will display to the user that the round is over and they have lost. 
      if bust ==1:
        #if bust is set to true, then the player busts and so, a message will display to user stating that the round is over. 
        print("Player busts! Round Over.")
        return 1
    print("\n")

    #Dealer's cards are shown
    self.dealer.showCards()

    #If 1 is returned from the player class, then the dealer has won the round of blackjack
    if dealer_hand == 1:
      #message displays to the user that the dealer got blackjack
      print("Dealer got Blackjack!")
      return 1

    #loop carried out to ensure that while the dealer's hand is less than 17, they can hit. 
    #If over 17, then the dealer will need to stand.
    while self.dealer.checkScore() < 17:
      if self.dealer.hit() ==1:
        #Dealer's cards will display
        self.dealer.showCards()
        #message to display that the dealer has lost the round of black jack 
        print("Dealer busts! You Win!")
        return 1
      #Dealer's cards are shown 
      self.dealer.showCards()

    #if the dealer's score is equal to the players score, then the game will tie or "push" and the game will end and display the end message
    if self.dealer.checkScore() == self.player.checkScore():
      print("It's a Push! Both player and dealer win!")
    #if the dealer's score is greater than the player's then the dealer wins blackjack and a message will display to user
    elif self.dealer.checkScore() > self.player.checkScore():
      print("Dealer Wins! Congratulations!")
    #if the player's score is greater than the dealer's, then the player will win the blackjack game and a corresponding message will display to the user
    elif self.dealer.checkScore() < self.player.checkScore():
      print("Player Wins! Congratulations!")
  
##setting the variable 'b' to the blackjack class
b =blackjack()
##Calling thr play method in the blackjack class. Program starts when this code is ran.
b.play()