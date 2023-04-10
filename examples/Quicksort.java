import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Quicksort {
    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);

        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);
        return i + 1;
    }

    static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int part = partition(arr, low, high);
            quickSort(arr, low, part - 1);
            quickSort(arr, part + 1, high);
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

        quickSort(arr, 0, len - 1);

        for (int i = 0; i < len; i++) {
            System.out.print(arr[i]);
            if (i < len - 1) {
                System.out.print(", ");
            }
        }

        System.out.println();
    }
}
