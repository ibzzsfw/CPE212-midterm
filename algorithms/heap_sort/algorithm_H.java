// Algorithm H (Max-Heapify)
public class algorithm_H {
    static void algorithmH(int arr[], int n, int i) {
        // Initialize
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        // Check left
        if (l < n && arr[l] > arr[largest])
            largest = l;

        // Check right
        if (r < n && arr[r] > arr[largest])
            largest = r;

        // Compare
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;
            algorithmH(arr, n, i);
        }
    }
}
