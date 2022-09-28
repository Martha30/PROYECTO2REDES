from jugador import Jugador
from bajara import Cartas
from mesa import *
from utilidades import *

class Juego:
   def __init__(self):
      self.mesa=Mesa(Cartas.FRANCESA52)
      self.jugadores=[]
      self.iniciarJugadores(4)
     

      self.mesa.mezclar()

      self.repartirCartas()
      
      for i in range(10):
         self.mesa.ponerCarta(self.mesa.mazo.pop(0))
   
   def ronda(self):
      print(Colores.BOLD+"Cartas en el tablero"+Colores.END)
      self.mesa.mostrarMesa(seleccion=True)
      for jugador in self.jugadores:
         self.jugar(jugador)
   
   def jugar(self, jugador):
      if jugador.esHumano():
         print("\r\n"+jugador.nombre+"\r\n"+Colores.BOLD+"Tus cartas"+Colores.END)
         jugador.mostrarMano(seleccion=True)
         opcion=Utilidades.preguntarOpciones("Que quieres hacer [C: escoger de mesa, T: Tirar]: ",["T","C", "V"])
         print("la opcion escogida es "+opcion)
         if(opcion=="C"):
            print("Cartas en la mesa")
            self.mesa.mostrarMesa(seleccion=True)
            numeroCartasEnMesa=len(self.mesa.cartaSobre)
            posCartaEscogida=Utilidades.preguntarNumero("Que carta escoges: (indica "+str(numeroCartasEnMesa)+" para escoger todas las cartas) ",1,numeroCartasEnMesa+1)

            if(posCartaEscogida<=numeroCartasEnMesa):
               
               if not self.esseleccionarCarta(jugador,posCartaEscogida):
                  print("La carta escogida no es válida. Debes poseer una carta de valor "+str(self.mesa.cartaSobre[posCartaEscogida-1].valor))
                  return False

            else:
               if not self.escogerTodas(jugador):
                  print("No puedes escoger todas las cartas")
                  return False
                           
               

         elif(opcion=="T"):
            posCartaEscogida=Utilidades.preguntarNumero("Que carta quieres tirar: ",1,len(jugador.mano))
            self.mesa.ponerCarta(jugador.mano.pop(posCartaEscogida-1))
         elif(opcion=="V"):
            jugador.mostrarCuenta()
            return False
      else:
         #Jugamos como bot
         self.jugarBot(jugador)
      #Comprobamos si el juegados se queda sin cartas en la mano. Si es así repartimos 4 a todos los jugadores
      if(jugador.numeroCartasEnMano()==0):
         self.repartirCartas()
      return True
   
   def jugarBot(self, jugador):
      print("\r\n"+jugador.nombre)
      if(jugador.numeroCartasEnMano()>0):
         if self.escogerTodas(jugador,mostrar=True):
            return True
         for i,carta in enumerate(self.mesa.cartaSobre):
            if self.esseleccionarCarta(jugador,i+1,mostrar=True):
               return True
         print(Colores.BOLD+"Tira la carta "+Colores.END)
         jugador.mano[0].mostrar()
         self.mesa.ponerCarta(jugador.mano.pop(0))
      return True


   def esseleccionarCarta(self,jugador,posCartaEscogida, mostrar=False):
      cartaEscogida=self.mesa.cartaSobre[posCartaEscogida-1]
      numeroCartasEnMesa=self.mesa.numeroCartasEnMesa()
      cartaEnMano=self.cartasEscogidasValidas(jugador,[cartaEscogida])
      if(cartaEnMano<0): 
         return False
      else:
         if mostrar:
            print("Se ha escogido una carta [Mesa: "+self.mesa.cartaSobre[posCartaEscogida-1].etiqueta+" - Mano: "+jugador.mano[cartaEnMano].etiqueta+"]")

         jugador.sumarPuntuacion(2+(1 if numeroCartasEnMesa==1 else 0))
         jugador.ponerCartaCuenta(self.mesa.cartaSobre.pop(posCartaEscogida-1))
         jugador.ponerCartaCuenta(jugador.mano.pop(cartaEnMano))
      return True

   def escogerTodas(self,jugador,mostrar=False):
      numeroCartasEnMesa=self.mesa.numeroCartasEnMesa()
      jugador.sumarPuntuacion(1+numeroCartasEnMesa+1)
      cartaEscogidaEnMano=self.cartasEscogidasValidas(jugador,self.mesa.cartaSobre)
      if cartaEscogidaEnMano>=0:
         cadena="Se ha barrido la mesa, las cartas son ["
         for i in range(numeroCartasEnMesa):
            carta=self.mesa.cartaSobre.pop(0)
            cadena+=(", " if i>0 else "")+carta.etiqueta
            jugador.ponerCartaCuenta(carta)
         if mostrar:
            print(cadena+"] y en la Mano: "+jugador.mano[cartaEscogidaEnMano].etiqueta)

         jugador.ponerCartaCuenta(jugador.mano.pop(cartaEscogidaEnMano)) 
         return True
      return False
      
   def cartasEscogidasValidas(self, jugador, cartasEscogidas):

      if(len(cartasEscogidas)==1):
         return jugador.poseeValorCarta(cartasEscogidas[0].valor)
      else:
         
         sumaCartas=0
         for carta in cartasEscogidas:
            if(type(carta.valor) == str):
               return -1
            sumaCartas+=carta.valor
         cartaValida=jugador.poseeValorCarta(sumaCartas)
         if(cartaValida>=0):
            return cartaValida
        
         for i, carta in enumerate(cartasEscogidas):
           
            cartaValida=jugador.poseeValorCarta(carta.valor)
            if(cartaValida>=0):
              
               sumaCartas=0
               for j,x in enumerate(cartasEscogidas):
                  if j!=i:
                     sumaCartas+= x.valor
               if sumaCartas==carta.valor:
                  return i
         return -1


   def iniciarJugadores(self, jugadoresTotales):
      numJugadores=Utilidades.preguntarNumero("Número de jugadores humanos: [0,"+str(jugadoresTotales)+"]",0,jugadoresTotales)
      for i in range(numJugadores):
         nombre =input("Nombre del jugador "+str(i+1)+": ")
         self.jugadores.append(Jugador(nombre,False))
      for i in range(jugadoresTotales-numJugadores):
         self.jugadores.append(Jugador("BOT_"+str(i+1),True))

   def repartirCartas(self):
      for _ in range(2):
         for jugador in self.jugadores:
            for _ in range(2):
               if(self.mesa.numeroCartasBaraja()>0):
                  jugador.seleccionarCarta(self.mesa.robar())
   def terminado(self):
      if(self.mesa.numeroCartasBaraja()==0):
         cartasEnMano=0
         for jugador in self.jugadores:
            cartasEnMano+=jugador.numeroCartasEnMano()
         return cartasEnMano==0
      
      return False
   def obtenerGanador(self):
      ganadores=[self.jugadores[0]]
      puntuacionMaxima=ganadores[0].obtenerPuntuacion()
      for jugador in self.jugadores[1:]:
         puntuancion=jugador.obtenerPuntuacion()
         if puntuancion>puntuacionMaxima:
            ganadores=[jugador]
            puntuacionMaxima=puntuancion
         elif puntuancion==puntuacionMaxima:
            ganadores.append(jugador)
      return ganadores