
 
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Conteo
{
    /*
     `arr` ——> la array de enteros de entrada que se va a ordenar
       `k` ——> un número tal que todos los enteros están en el rango `0…k-1`
    */
    public static void conteo(int[] arr, int k)
    {
        // crea una array de enteros de tamaño `n` para almacenar la array ordenada
        int[] output = new int[arr.length];
 
        // crea una array de enteros de tamaño `k + 1`, inicializada por todos cero
        int[] freq = new int[k + 1];
 
        // usando el valor de cada elemento en la array de entrada como índice,
        // almacena el conteo de cada entero en `freq[]`
        for (int i: arr) {
            freq[i]++;
        }
 
        // calcular el índice inicial para cada entero
        int total = 0;
        for (int i = 0; i < k + 1; i++)
        {
            int oldCount = freq[i];
            freq[i] = total;
            total += oldCount;
        }
 
        // copia a la array de salida, conservando el orden de las entradas con claves iguales
        for (int i: arr)
        {
            output[freq[i]] = i;
            freq[i]++;
        }
 
        // copia la array de salida de nuevo a la array de entrada
        Arrays.setAll(arr, i -> output[i]);
    }
 
    public static void main(String[] args) throws IOException { 
 
        final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        final String consoleInput = reader.readLine();
        
        final String[] tokens = consoleInput.split(" ");
        int[] arr = new int[tokens.length];
        for (int i = 0; i < tokens.length; i++) {
        	arr[i] = Integer.parseInt(tokens[i]);
        }
        
        int len = arr.length;
    
        conteo(arr, len);

        for (int i = 0; i < len; i++) {
            System.out.print(arr[i]);
            if (i < len - 1) {
                System.out.print(" ");
            }
        }}}