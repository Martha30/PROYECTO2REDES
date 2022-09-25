from jugador import Jugador,jugadores
from tablero import *

print("BIENVENIDOS AL JUEGO")
tablero=Tablero()
Jugador.iniciarJugadores()
tablero.mezclar()
#print(len(tablero.mazo))
print(jugadores)
#print("LA PRIMERA CARTA ES "+tablero.mostrar())


