class Card:
    """ Represents a card from a deck of cards.
    """
  
    # Here are some class variables
    # to represent possible suits and ranks
    suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]  

    def __init__(self, suit=0, rank=0):
        """ Create a card using integer variables to represent suit and rank.
        """
        # Couple of handy asserts to check any cards we build make sense
        assert suit >= 0 and suit < 4  
        assert rank >= 0 and rank < 14
        
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        # The lookup in the suits/ranks lists prints 
        # a human readable representation of the card.
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])
      
    def same_color(self, other):
      """ Returns the True if cards have the same color else False
      Diamonds and hearts are both read, clubs and spades are both black.
      """
      return self.rank == other.rank or self.rank == (other.rank + 2) % 4
    
    # The following methods implement card comparison
    
    def cmp(self, other):
      """ Compares the card with another, returning 1, 0, or -1 depending on 
      if this card is greater than, equal or less than the other card, respectively.
      
      Cards are compared first by suit and then rank.
      """
      # Check the suits
      if self.suit > other.suit: return 1
      if self.suit < other.suit: return -1
      # Suits are the same... check ranks
      if self.rank > other.rank: return 1
      if self.rank < other.rank: return -1
      # Ranks are the same... it's a tie
      return 0
  
  
    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0
    
x = Card(2, 1)
y = Card(2, 13)

#print("x is:", x)
#print("y is:", y)
#print("x is less than y:", x < y) # Aces low.
  
  