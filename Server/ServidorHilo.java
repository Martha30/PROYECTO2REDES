import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.net.Socket;
import java.util.ArrayList;

public class ServidorHilo extends Thread{
    
    private Socket sc;
    private DataInputStream in;
    private DataOutputStream out;
    private String nombreCliente = null;

    public ServidorHilo(Socket sc, DataInputStream in, DataOutputStream out, String nombreCliente) {
        this.sc = sc;
        this.in = in;
        this.out = out;
        this.nombreCliente = nombreCliente;
    }

    @Override
    public void run(){

        int option;
        File f = new File("numeros.txt");
        boolean salir = false;
        while(!salir){

            try {
                option = in.readInt();

                switch(option){
                    case 1:
                        int numeroaleatorio = in.readInt();
                        escribirNumeroAleatorio(f, numeroaleatorio);
                        out.writeUTF("Numero guardado correctamente");
                        System.out.println("Se escribio el numero en el cliente " + nombreCliente);
                        break;
                    case 2:
                        int numLineas = numeroLineasFichero(f);
                        out.writeInt(numLineas);
                        break;
                    case 3:
                        ArrayList<Integer> numeros = listaNumeros(f);
                        out.writeInt(numeros.size());

                        for (int n:numeros){
                            out.writeInt(n);
                        }

                        break;
                    case 4:
                        int numLineasCliente = numeroLineasFicheroCliente(f);
                        out.writeInt(numLineasCliente);
                        break;
                    case 5:
                        byte[] contenidoFichero = ficheroNumeroCliente(f);
                        out.writeInt(contenidoFichero.length);

                        for (int i = 0; i < contenidoFichero.length; i++){
                            out.writeByte(contenidoFichero[i]);
                        }

                        break;
                    case 6:
                        salir=true;
                        break;
                    default:
                        out.writeUTF("Solo numeros del 1 al 6");
                        
                }

            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }

        }
        try {
            sc.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        System.out.println("Conexion cerrada con el cliente " + nombreCliente);
    }

    public void escribirNumeroAleatorio(File f, int numeroaleatorio) throws IOException{

        FileWriter fw = new FileWriter(f, true);
        fw.write(nombreCliente + ":" + numeroaleatorio + "\r\n");
        fw.close();

    }

    public int numeroLineasFichero(File f) throws IOException{
        int numLineas = 0;
        BufferedReader br = new BufferedReader(new FileReader((f)));

        String linea = "";
        
        while ((linea = br.readLine()) != null){
            numLineas++;
        }

        br.close();
        return numLineas;
    }

    public ArrayList<Integer> listaNumeros(File f) throws IOException{
        ArrayList<Integer> numeros = new ArrayList<>();

        BufferedReader br = new BufferedReader(new FileReader((f)));

        String linea = "";
        
        while ((linea = br.readLine()) != null){
            String[] partes = linea.split(":");

            int numero = Integer.parseInt(partes[1]);
            numeros.add(numero);
        }

        br.close();

        return numeros;
    }

    public int numeroLineasFicheroCliente(File f) throws IOException{
        int numLineas = 0;
        BufferedReader br = new BufferedReader(new FileReader((f)));

        String linea = "";
        
        while ((linea = br.readLine()) != null){

            String[] partes  = linea.split(":");
            if (partes[0].equals(nombreCliente)){
                numLineas++;
            }

        }

        br.close();
        return numLineas;
    }

    public byte[] ficheroNumeroCliente(File f) throws IOException{
        int numLineas = 0;
        BufferedReader br = new BufferedReader(new FileReader((f)));

        String linea = "";
        String contenido = "";
        
        while ((linea = br.readLine()) != null){

            String[] partes  = linea.split(":");
            if (partes[0].equals(nombreCliente)){
                contenido += linea + "\r\n";
            }

        }

        br.close();

        return contenido.getBytes();
    }

}
