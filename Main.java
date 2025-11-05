import java.util.Arrays;

public class Main {

    /* ---------------------- ПИРАМИДАЛЬНАЯ СОРТИРОВКА ---------------------- */

    // Преобразует поддерево с корнем root в кучу (heapify)
    public static void heapify(int[] arr, int n, int root) {
        int largest = root;           // Считаем корень наибольшим
        int left = 2 * root + 1;      // Индекс левого потомка
        int right = 2 * root + 2;     // Индекс правого потомка

        // Проверяем, существует ли левый потомок и больше ли он корня
        if (left < n && arr[left] > arr[largest])
            largest = left;

        // Проверяем правого потомка
        if (right < n && arr[right] > arr[largest])
            largest = right;

        // Если корень не самый большой — меняем местами и продолжаем
        if (largest != root) {
            int temp = arr[root];
            arr[root] = arr[largest];
            arr[largest] = temp;

            heapify(arr, n, largest); // Рекурсивно восстанавливаем кучу
        }
    }

    // Основная процедура пирамидальной сортировки
    public static void heapSort(int[] arr) {
        int n = arr.length;

        // Строим начальную max-кучу
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);

        // Извлекаем элементы из кучи один за другим
        for (int i = n - 1; i > 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            heapify(arr, i, 0);
        }
    }

    /* ---------------------- СОРТИРОВКА ПУЗЫРЬКОМ ---------------------- */

    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;

        // Проходим по массиву несколько раз
        for (int i = 0; i < n - 1; i++) {
            swapped = false;

            for (int j = 0; j < n - i - 1; j++) {
                // Если соседние элементы не по порядку — меняем их
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // Если обменов не было — массив уже отсортирован
            if (!swapped) break;
        }
    }

    /* ---------------------- СОРТИРОВКА ВЫБОРОМ ---------------------- */

    public static void selectionSort(int[] array) {
        int n = array.length;

        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;

            // Ищем наименьший элемент в неотсортированной части массива
            for (int j = i + 1; j < n; j++) {
                if (array[j] < array[minIndex])
                    minIndex = j;
            }

            // Меняем местами текущий элемент и найденный минимум
            int temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }

    /* ---------------------- ЛИНЕЙНЫЙ ПОИСК ---------------------- */

    // Последовательно проверяет каждый элемент массива
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target)
                return i; // Возвращаем индекс найденного элемента
        }
        return -1; // Если элемент не найден
    }

    /* ---------------------- ОСНОВНОЙ МЕТОД ---------------------- */

    public static void main(String[] args) {

        // 1. Пирамидальная сортировка
        int[] heapArray = {12, 11, 13, 5, 6, 7};
        System.out.println("Исходный массив (пирамидальная сортировка): " + Arrays.toString(heapArray));
        heapSort(heapArray);
        System.out.println("После сортировки: " + Arrays.toString(heapArray));
        System.out.println();


        // 2. Пузырьковая сортировка
        int[] bubbleArray = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("Исходный массив (пузырьковая сортировка): " + Arrays.toString(bubbleArray));
        bubbleSort(bubbleArray);
        System.out.println("После сортировки: " + Arrays.toString(bubbleArray));
        System.out.println();


        // 3. Сортировка выбором
        int[] selectionArray = {64, 25, 12, 22, 11};
        System.out.println("Исходный массив (сортировка выбором): " + Arrays.toString(selectionArray));
        selectionSort(selectionArray);
        System.out.println("После сортировки: " + Arrays.toString(selectionArray));
        System.out.println();


        // 4. Линейный поиск
        int[] data = {3, 7, 1, 9, 5};
        int target = 9;

        System.out.println("Массив для линейного поиска: " + Arrays.toString(data));
        int result = linearSearch(data, target);

        if (result != -1)
            System.out.println("Элемент " + target + " найден на индексе: " + result);
        else
            System.out.println("Элемент " + target + " не найден.");
    }
}
