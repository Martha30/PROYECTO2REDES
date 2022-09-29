from Deck import Deck

class Hand(Deck):
    
    def __init__(self, name=""):
      """ Creates an initially empty set of cards.
      """
      self.cards = []
      self.name = name
    
    def __str__(self):
      s = "Hand " + self.name
      if self.is_empty():
          s += " is empty\n"
      else:
          s += " contains\n"
      return s + Deck.__str__(self)
  
