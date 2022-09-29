import random
from Card import Card

class Deck:
    """ Represents a deck of cards.
    """
  
    def __init__(self):
        """ Creates a full set of cards"""
        self.cards = [] # cards stores the list of cards
        for suit in range(4): # Note the nested for loops
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
    
    def __str__(self):
        s = "" # Builds a deck of cards, laying them out diagonally 
        # across the screen.
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s
      
    def __len__(self):
        return len(self.cards)
    
    def shuffle(self):
        """ Shuffles the cards into a random order
        """
        rng = random.Random()        # Create a random generator
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = rng.randrange(i, num_cards)
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])
    
    def remove(self, card):
        """ Removes the card from the deck. Returns True if successful. """
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False
          
    def pop(self):
        """ Removes the last card in the deck and returns it."""
        return self.cards.pop()
    
    def add(self, card):
        """ Adds the card to the deck. """
        assert card not in self.cards # We include this check here
        # because we want to protect against having the same card
        # in the deck twice
        self.cards.append(card)
      
    def is_empty(self):
        """ Returns True if the deck is empty."""
        return self.cards == []
      
    def deal(self, hands, num_cards_per_hand=999):
        """ Deals cards into hands. num_cards_per_hand 
        is number of cards per hand"""
        num_hands = len(hands)
        for i in range(num_cards_per_hand * num_hands):
            if self.is_empty():
                break                    # Break if out of cards
            card = self.pop()            # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)               # Add the card to the hand
            
