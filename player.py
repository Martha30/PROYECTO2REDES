import random

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        
    def print_card(self):
        for card in self.cards:
            print(card.get_card_text(), card.typeC)
            
    def prompt_card(self,previous_card):
        if previous_card != None:
            print("Escribe la carta a hacer match: " + str(previous_card.get_card_text(), previous_card.typeC))
        card = input("Escribe la carta que quieras emparejar: formato: numero/letra - tipo de carta:  n/Si no hay una carta que haga match, escribe draw para elegir una carta: ")
        while not self.check_card_exist(card,previous_card):
            self.print_card()
            if card == "draw":
                self.draw_card()
            else:
                print("Carta no encontrada o no se puede emparejar!!")
            card = input("Escribe la carta que quieras emparejar: formato: numero/letra - tipo de carta: ")
        return self.remove_card(card)

            
        
    def check_card_exist(self, card: str, previous_card):
        for c in self.cards:
            if previous_card != None:
                if str(c) == card and (previous_card.typeC == c.typeC or previous_card.number == c.number):
                    return True
            else:
                if str(c) == card:
                    return True
        return False
    
    def remove_card(self, card: str):
        for c in self.cards:
            if str(c) == card:
                self.cards.remove(c)
                break;
            
    def draw_card(self,card):
        self.cards.append(self.deck[random.randint(0, len(self.deck)-1)])
        