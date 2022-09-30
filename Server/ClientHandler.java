import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Array;
import java.net.Socket;
import java.util.ArrayList;

public class ClientHandler implements Runnable {

    public static ArrayList<ClientHandler> clientHandlers = new ArrayList<>(); 
    private Socket socket;
    private BufferedReader bufferedReader;
    private BufferedWriter bufferedWriter;
    private String clientUsername;
    private String room;
    private User[] newRoom = new User[4];

    public ClientHandler(Socket socket){
        try{
            this.socket = socket;
            this.bufferedWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            this.bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.clientUsername = checkNames();
            clientHandlers.add(this);
            broadcastMessage("SERVER: " + clientUsername + " has entered the chat!");
        } catch (IOException e){
            closeEverything(socket, bufferedReader, bufferedWriter);
        }
    }

    @Override
    public void run() {
        // TODO Auto-generated method stub
        String messageFromClient;

        while(socket.isConnected()){
            try{
                messageFromClient = bufferedReader.readLine();
                switch (messageFromClient){
                    case "1":
                        setRoom(bufferedReader.readLine());
                        break;
                    case "2":
                        joinRoom(bufferedReader.readLine());
                        break;
                    case "3":
                        break;
                }
                // broadcastMessage(messageFromClient);
            }catch (IOException e){
                closeEverything(socket, bufferedReader, bufferedWriter);
                break;
            }
        }
    }

    public void joinRoom(String codigo) throws IOException{
        for (ClientHandler clientHandler: clientHandlers){
            if (clientHandler.room == null){
                break;
            }
            if (clientHandler.room.equals(codigo)){
                for(int i = 0; i<clientHandler.newRoom.length; i++){
                    if (clientHandler.newRoom[i] == null){
                        User usuario = new User(clientUsername, socket, clientHandler.newRoom[i-1].getNumero() + 1);
                        clientHandler.newRoom[usuario.getNumero()] = usuario;

                        bufferedWriter.write("Ha ingresado a la sada de " + clientHandler.clientUsername);
                        bufferedWriter.newLine();
                        bufferedWriter.flush();
                        clientHandler.bufferedWriter.write("Ha ingresado a la sala " + clientUsername);
                        clientHandler.bufferedWriter.newLine();
                        clientHandler.bufferedWriter.flush();
                        break;
                    }else {
                        bufferedWriter.write("La sala se encuentra llena, pruebe con otra sala");
                        bufferedWriter.newLine();
                        bufferedWriter.flush();
                    }
                }
            }
        }
    }

    public void setRoom(String codigo) throws IOException{
        for (ClientHandler clientHandler: clientHandlers){
            if (clientHandler.clientUsername.equals(clientUsername)){
                clientHandler.room = codigo;
                User usuario = new User(clientUsername, socket, 0);
                newRoom[usuario.getNumero()] = usuario;
                bufferedWriter.write("Ha creado correctamente una sala!");
                bufferedWriter.newLine();
                bufferedWriter.flush();
            }
        }
    }

    public void broadcastMessage(String messageToSend){
        for (ClientHandler clientHandler: clientHandlers){
            try{
                if (!clientHandler.clientUsername.equals(clientUsername)){
                    clientHandler.bufferedWriter.write(messageToSend);
                    clientHandler.bufferedWriter.newLine();
                    clientHandler.bufferedWriter.flush();
                }
            }catch (IOException e){
                closeEverything(socket, bufferedReader, bufferedWriter);
            }
        }
    }

    public String checkNames() throws IOException{
        final String[] name = new String[1];
        boolean repetido = true;
        name[0] = "";
        while (repetido){

            name[0] = bufferedReader.readLine();
            if (clientHandlers.isEmpty()){
                repetido = false;
                bufferedWriter.write("Ha ingresado exitosamente al servidor!");
                bufferedWriter.newLine();
                bufferedWriter.flush();
            }else{
                for (ClientHandler clientHandler: clientHandlers){
                    if (!clientHandler.clientUsername.equals(name[0])){
                        repetido = false;
                        bufferedWriter.write("Ha ingresado exitosamente al servidor!");
                        bufferedWriter.newLine();
                        bufferedWriter.flush();
                    }
                }
                if (repetido){
                    bufferedWriter.write("Ese nombre ya existe en el servidor elija otro nombre:");
                    bufferedWriter.newLine();
                    bufferedWriter.flush();
                }
            }
        }
        return name[0];
    }

    public void removeClienteHandler(){
        clientHandlers.remove(this);
        broadcastMessage("SERVER: " + clientUsername + " has left the chat!");
    }

    public void closeEverything(Socket socket, BufferedReader bufferedReader, BufferedWriter bufferedWriter){
        removeClienteHandler();
        try{
            if ( bufferedReader != null){
                bufferedReader.close();
            }
            if (bufferedWriter != null){
                bufferedWriter.close();
            }
            if (socket != null){
                socket.close();
            }
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
