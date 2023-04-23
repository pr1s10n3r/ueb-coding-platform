import java.util.Arrays;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
 
 class InsertionSort
{
    // Función para realizar ordenación por inserción en `arr[]`
    public static void insercion(int[] arr)
    {
        // Empezar desde el segundo elemento
        // (el elemento en el índice 0 ya está ordenado)
        for (int i = 1; i < arr.length; i++)
        {
            int value = arr[i];
            int j = i;
 
            // encuentra el índice `j` dentro del subconjunto ordenado `arr[0…i-1]`
            // donde pertenece el elemento `arr[i]`
            while (j > 0 && arr[j - 1] > value)
            {
                arr[j] = arr[j - 1];
                j--;
            }
 
            // tenga en cuenta que el subarray `arr[j…i-1]` se desplaza a
            // la derecha por una posición, es decir, `arr[j+1…i]`
 
            arr[j] = value;
        }
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
    
        insercion(arr);

        for (int i = 0; i < len; i++) {
            System.out.print(arr[i]);
            if (i < len - 1) {
                System.out.print(" ");
            }
        }
    }
    }
