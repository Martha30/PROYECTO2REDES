from card import Card
import subprocess
import os


def create_all_cards():
    rojo = "rojo"
    negro = "negro"
    deck = []
    for typeC in ["corazones rojas", "diamantes rojas", "picas negras", "treboles negras"]:
        for number in range(1, 10):
            deck.append(Card(typeC, number, None))
        for special_ability in ["A", "J", "K", "Q"]: 
            deck.append(Card(typeC, special_ability=special_ability))
                 
    deck.append(Card(special_ability="Joker"))
        
    return deck

    

def cls():
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120