from CardGame import CardGame
from Card import Card
from Deck import Deck
from Hand import Hand
from OldMaidHand import OldMaidHand

class OldMaidGame(CardGame):
    def __init__(self, names):
        """ Construct a game of Old Maid, each name
        in names is the name of a player.
        """
        CardGame.__init__(self) #Call the base class constructor
        
        # Remove Queen of Clubs (so Queen of Spades is Old Maid)
        self.deck.remove(Card(0,12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))
        
    def play(self, interactive=False):
        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        # Remove initial matches
        count = 1 # Count of discarded cards (1 to start, 
        # representing discarded queen)
        for hand in self.hands:
            count += len(hand.remove_matches())
        print("---------- Matches discarded, play ready to begin")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while count < 51:
            count += self.play_one_turn(turn, interactive)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()
        
    def play_one_turn(self, i, interactive):
        """ Play one turn for the ith player
        """
        
        hand = self.hands[i]
        
        #if hand.is_empty(): # You can remove comments to allow players to get "out"
        #return 0
          
        # Find a neighboring hand with one or more cards
        neighbor = self.hands[self.find_neighbor(i)]
        
        if interactive:
            # Allow the user to pick the card to add to their deck
            while True:
                s = "{} enter a card choice from 1 to {} from {}'s hand:".\
                format(hand.name, len(neighbor.cards)-1, neighbor.name)
                user_value = input(s)
                try: # This is an example of exception handling, we'll cover this next time
                    j = int(user_value)
                except ValueError:
                    print("Invalid number", user_value)
                    continue
                if j < 1 or j > len(neighbor.cards)-1:
                    print("Invalid choice", j)
                    continue
                picked_card = neighbor.cards[j-1]
                del neighbor.cards[j-1]
                break
        else:
            # Else just pick one randomly
            picked_card = neighbor.pop()
            
        hand.add(picked_card)
        print("Hand", hand.name, "picked", picked_card, "from", neighbor.name)
        count = len(hand.remove_matches())
        
        hand.shuffle()
        
        return count
    
    def find_neighbor(self, i):
        """ Find the neighbor of the player without an empty hand 
        """
        num_hands = len(self.hands)
        for next in range(1,num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor
    
    def print_hands(self):
        for hand in self.hands:
            print(hand)
            
game = OldMaidGame(["Allen","Jeff","aa","bb"])
game.play(interactive=True)
    
    