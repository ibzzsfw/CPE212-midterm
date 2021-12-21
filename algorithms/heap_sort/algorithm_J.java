// algorithm J (Heap Sort)
public class algorithm_J {

    public void algorithmJ(int arr[]) {
        // Build
        int n = arr.length;
        for (int i = n / 2 - 1; i >= 0; i--)
            algorithmH(arr, n, i);
        // Heapify
        for (int i = n - 1; i > 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            algorithmH(arr, i, 0);
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