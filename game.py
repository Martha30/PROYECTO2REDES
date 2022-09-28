from player import Player
from helpers import cls
import random

class game:
    def __init__(self, player1: Player , player2: Player, player3: Player, player4: Player):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.previous_card = None
        
    def play(self):
        while not self.check_winning():
            
            rand = random.randint(1,4)

            
            print("Jugador 1, has tu jugada. ")
            self.player1.print_card()
            self.previous_card = self.player1.prompt_card((self.previous_card))
            
            #cls()
            
            print("Jugador 2, has tu jugada")
            self.player2.print_card()
            self.previous_card = self.player2.prompt_card((self.previous_card))
            
            #cls()

            print("Jugador 3, has tu jugada")
            self.player3.print_card()
            self.previous_card = self.player3.prompt_card((self.previous_card))
            
            #cls()

            
            print("Jugador 4, has tu jugada")
            self.player4.print_card()
            self.previous_card = self.player4.prompt_card((self.previous_card))
    
    def check_winning(self):
        if len(self.player1.cards) == 0:
            print("Jugador 1 Gana!")
            return True
        elif len(self.player2.cards) == 0:
            print("Jugador 2 Gana!")
            return True
        elif len(self.player3.cards) == 0:
            print("Jugador 3 Gana!")
            return True
        elif len(self.player4.cards) == 0:
            print("Jugador 3 Gana!")
            return True
        else:
            return False
        