from helpers import create_all_cards
import random

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.deck = create_all_cards()


    def print_cards(self):
        for card in self.cards:
            print(card.get_card_text(), card.typeC)

    def prompt_card(self, previous_card,game):
        if previous_card != None:
            print("Elegir primer carta a hacer match: (formato: numero/letra - tipo de carta y color): " + str(previous_card.get_card_text()), previous_card.typeC)
        card = input("Escribe la carta que quieras emparejar: (formato: numero/letra - tipo de carta y color):  Si no hay una carta que hagan match, escribe draw para elegir una carta del siguiente jugador: ")
        while not self.check_card_valid(card, previous_card, game):
            
            print("The previous card is: " + previous_card.get_card_text(), previous_card.typeC)
            self.print_cards()
            if card == "draw":
                self.draw_card()
            else:
                print("Carta no encontrada o no valida")
            card = input("Escribe la carta que quieras hacer match: (formato: numero/letra - tipo de carta y color): ")
        return self.remove_card(card)

    def check_card_valid(self, card: str, previous_card,game):
        for c in self.cards:
            if previous_card != None: # need to handle special card, such as everything, stack, etc.
                if str(c) == card and ((previous_card.typeC== c.typeC and previous_card.number == c.number) or (previous_card.typeC.__contains__("corazones rojas")==c.typeC.__contains__("diamentes rojas") and previous_card.number == c.number) or (previous_card.typeC.__contains__("picas negras")==c.typeC.__contains__("treboles negras") and previous_card.number == c.number)):
                    return True
            else:
                if str(c) == card:
                    return True
            # else:
            #     if str(c) == card:
            #         if c.special_ability == "reverse":
            #             game.reverse()
            #         if c.special_ability == "skip":
            #             game.skip()
            #         return True
        return False

    def remove_card(self, card: str):
        for c in self.cards:
            if str(c) == card:
                self.cards.remove(c)
                return c

    def draw_card(self):
        self.cards.append(self.deck[random.randint(0, len(self.deck) - 1)])