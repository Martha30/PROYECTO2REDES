
jugadores=[]

class Jugador:
    def _init_(self,nombre,esBot):
        self.nombre =nombre
        self.esBot=esBot

    @staticmethod
    def iniciarJugadores():
        numJugadores=int(input("NUMERO DE JUGADORES:"))
        for i in range(numJugadores):
            nombre=(input("NOMBRE DEL JUGADOR "+str(i+1)+":"))
            esBot=(input("¿Es BOT?[S/N]")=="S")
            jugadores.append(Jugador(nombre,esBot))
            