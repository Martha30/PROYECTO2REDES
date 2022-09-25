from bajara import *

class Tablero:
    def __init__(self):
        self.mazo=Carta.cargarCartas()
        self.cartaSobre=[]
    def mezclar(self):
        self.mazo=Carta.mezclar(self.mazo)
    def mostrar(self):
        return self.mazo[0].etiqueta