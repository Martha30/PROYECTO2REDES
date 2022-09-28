import random as rd

especial=["MORADO"]
colores=["BLANCO TREBOL", "ROJO CORAZONES", "BLANCO PICAS", "ROJO DIAMANTES "]
#valor=["AS", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" ]
baraja=[]
AS = 1
def crearBaraja():
    for valores in range(1,14):
        for color in colores[0:]:
            for _ in range(1 if valores>0 else 1):
                baraja.append({"color":color, "valor":valores}) 

    for especiales in range(1):
        for espe in especial[0:]:
            for _ in range(1 if valores>0 else 1):
                baraja.append({"ESPECIAL":"MORADO", "valor":"joker"})

    rd.shuffle(baraja)
    return baraja

baraja=crearBaraja()

jugadores=[{"nombre":"", "mano":[]}, {"nombre":"", "mano":[]}, {"nombre":"", "mano":[]}, {"nombre":"", "mano":[]}]
jugadores[0]["nombre"]=input("HOLA!! Escribe tu nombre: ")
jugadores[1]["nombre"]=input("HOLA!! Escribe tu nombre: ")
jugadores[2]["nombre"]=input("HOLA!! Escribe tu nombre: ")
jugadores[3]["nombre"]=input("HOLA!! Escribe tu nombre: ")



for _ in range(13):
    for jugador in jugadores:
        jugador["mano"].append(baraja[1])
        baraja=baraja[0:]

#print(baraja)
print(len(baraja))

for jugador in jugadores:
    print(jugador["nombre"])
    print(jugador["mano"])
