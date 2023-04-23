import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class BubbleSort {

	public void burbuja(int[] array) {
		for (int i = array.length - 1; i > 0; i--) {
			for (int j = 0; j < i; j++) {
				if (array[j] > array[j + 1]) {
					swap(array, j, j+1);
				}
				
			}
			
		}
	}

	

	public void swap(int[] array, int a, int b) {
		int value = array[b];
		array[b] = array[a];
		array[a] = value;
	}

	


    public static void main(String[] args) throws IOException {  
        BubbleSort bubbleSort = new BubbleSort();
        final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        final String consoleInput = reader.readLine();
        
        final String[] tokens = consoleInput.split(" ");
        int[] arr = new int[tokens.length];
        for (int i = 0; i < tokens.length; i++) {
        	arr[i] = Integer.parseInt(tokens[i]);
        }
        
        int len = arr.length;
    
        bubbleSort.burbuja(arr);

        for (int i = 0; i < len; i++) {
            System.out.print(arr[i]);
            if (i < len - 1) {
                System.out.print(" ");
            }
        }
    }
}