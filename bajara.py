import random as rd

class Carta:
   def __init__(self,etiqueta,valor,palo):
    #self.etiqueta = etiqueta
    #self.valor = valor
    #self.palo = palo

   @staticmethod
   def cargarCartas():
    #aqui se cargan y se definen las cartas y su valor
    baraja=[]
    for p in ['Picas', 'Corazones', 'Rombos', 'Treboles']:
        for i in range(1,14):
           baraja.append(Carta((str(i)+"" +p,i,p)))
        return baraja
    
   @staticmethod
   def mezclar(mazo):
    rd.shuffle(mazo)
    return mazo


