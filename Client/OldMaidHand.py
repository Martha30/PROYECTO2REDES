from Hand import Hand
from Deck import Deck
from Card import Card

class OldMaidHand(Hand):
    """ Old Maid version of a hand.
    """
    
    def remove_matches(self):
       
        removed_cards = []
        for card in self.cards[:]: 
            
            match = Card((card.suit + 2) % 4, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                removed_cards.append(card)
                removed_cards.append(match)
                print("Hand {0}: {1} matches {2}"
                        .format(self.name, card, match))
                
        return removed_cards 
    
