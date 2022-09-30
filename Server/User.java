import java.net.Socket;

public class User {
    private String Nombre;
    private Socket socket;
    private int Numero;
    public int getNumero() {
        return Numero;
    }
    public void setNumero(int numero) {
        Numero = numero;
    }
    public User(String nombre, Socket socket, int Numero) {
        Nombre = nombre;
        this.socket = socket;
        this.Numero = Numero;
    }
    public String getNombre() {
        return Nombre;
    }
    public void setNombre(String nombre) {
        Nombre = nombre;
    }
    public Socket getSocket() {
        return socket;
    }
    public void setSocket(Socket socket) {
        this.socket = socket;
    }
}
