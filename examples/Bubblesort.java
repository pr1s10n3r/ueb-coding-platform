package me.astagg;

public class BubbleSort<T> {
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

	static void printArray(String msg, int[] arr) {
		System.out.println(msg);
		
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i]);
			if (i < arr.length - 1) {
				System.out.print(", ");
			}
		}

		System.out.println();
	}

	public static void main(String[] args) {
		int[] arr = { 0, 6, 5, 1, 2, 83, 55, 100, 662, -1, 7 };
		printArray("Before bubble sort:", arr);
		int[] sorted = bubbleSort(arr);
		printArray("After bubble sort:", sorted);
	}
}
