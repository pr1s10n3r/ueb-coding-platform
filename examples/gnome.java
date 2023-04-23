
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class GFG {
 static void gnome(int arr[], int n)
 {
  int index = 0;
 
  while (index < n) {
   if (index == 0){
    index++;}
   if (arr[index] >= arr[index - 1]){
    index++;}
   else {
    int temp = 0;
    temp = arr[index];
    arr[index] = arr[index - 1];
    arr[index - 1] = temp;
    index--;
   }
  }
  return;
 }
 
 // Driver program to test above functions.
 public static void main(String[] args)throws IOException { 
 
        final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        final String consoleInput = reader.readLine();
        
        final String[] tokens = consoleInput.split(" ");
        int[] arr = new int[tokens.length];
        for (int i = 0; i < tokens.length; i++) {
        	arr[i] = Integer.parseInt(tokens[i]);
        }
        
        int len = arr.length;
    
        gnome(arr, len);

        for (int i = 0; i < len; i++) {
            System.out.print(arr[i]);
            if (i < len - 1) {
                System.out.print(" ");
            }
        }
    }
 
  
 
  
 }

 