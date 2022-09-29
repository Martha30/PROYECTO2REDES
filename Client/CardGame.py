from Deck import Deck
class CardGame:
    """ Represents a card game. Designed
    to be inherited by more specific, complete games
    """
    
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()