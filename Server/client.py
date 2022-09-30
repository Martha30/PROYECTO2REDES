import socket
import threading
import random

#config socket
IP = socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

# Clase cliente que guarda sus datos
class client:
    def __init__(self, username, socket, isConnected):
        self.username = username
        self.socket = socket
        self.isConnected = isConnected

def sendMessage(cliente):
    while cliente.isConnected:
        message = input("type your message and press enter to send....\n")
        cliente.socket.sendall((cliente.username+ ": " +message+'\n').encode(FORMAT))

def listenForMessage(socket, isConnected):
    while isConnected:
        data = socket.recv(SIZE).decode(FORMAT)
        print(data)

def menu(cliente):
    print("1. Crear sala")
    print("2. Unirse a sala sala")
    print("3. Salir")
    option = input("> ")
    cliente.socket.sendall((option+'\n').encode(FORMAT))
    if option == "1":
        codigo = generarCodigo(6)
        print("El codigo de tu sala es: %s" %(codigo))
        cliente.socket.sendall((codigo+'\n').encode(FORMAT))
        t = threading.Thread(target=listenForMessage, args=(cliente.socket, cliente.isConnected))
        t.start()
    elif option == "2":
        codigo = input("Ingrese el codigo para ingresar a la sala: ")
        cliente.socket.sendall((codigo+'\n').encode(FORMAT))
        t = threading.Thread(target=listenForMessage, args=(cliente.socket, cliente.isConnected))
        t.start()
    elif option == "3":
        pass
    else: 
        print("Elija una de las opciones")

def generarCodigo(length):
    result = ""
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    charactersLength = len(characters)
    for i in range(0, length):
        result += characters[random.randint(0, charactersLength-1)]
    return result


def main():
    username = input("Enter your username to enter: \n")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ADDR)
    cliente = client(username, s, True)
    cliente.socket.sendall((cliente.username+'\n').encode(FORMAT))
    data = cliente.socket.recv(SIZE).decode(FORMAT)
    print(data)
    if data == "Ese nombre ya existe en el servidor elija otro nombre:\n":
        repetido = True
        while repetido:
            username = input("Enter another username to enter: \n")
            cliente.socket.sendall((username+'\n').encode(FORMAT))
            data = cliente.socket.recv(SIZE).decode(FORMAT)
            print(data);
            if data == "Ha ingresado exitosamente al servidor!\n":
                repetido = False
        
    menu(cliente)
    # sendMessage(cliente)
    
main()