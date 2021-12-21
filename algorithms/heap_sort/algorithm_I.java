// Algorithm I (Build-Max-Heap)
public class algorithm_I {

    static void AlgorithmI(int arr[], int n) {
        // Initialize
        int startIdx = (n / 2) - 1;
        for (int i = startIdx; i >= 0; i--) {
            // Max-Heapify
            algorithmH(arr, n, i);
        }
    }

    static void algorithmH(int arr[], int n, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && arr[l] > arr[largest])
            largest = l;
        if (r < n && arr[r] > arr[largest])
            largest = r;
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;
            algorithmH(arr, n, i);
        }
    }
}
