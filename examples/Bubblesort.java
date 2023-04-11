import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bubblesort {
	static int[] bubbleSort(int[] arr) {
		int[] sorted = arr;

		for (int i = 0; i < sorted.length - 1; i++) {
			for (int j = i + 1; j < sorted.length; j++) {
				if (arr[j] < arr[i]) {
					int tmp = sorted[j];
					sorted[j] = sorted[i];
					sorted[i] = tmp;
				}
			}
		}

		return sorted;
	}

	static void printArray(int[] arr) {
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i]);
			if (i < arr.length - 1) {
				System.out.print(" ");
			}
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

		int[] sorted = bubbleSort(arr);
		printArray(sorted);
	}
}
