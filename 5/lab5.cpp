#include <iostream>
using namespace std;

/* ---------------------- БЫСТРАЯ СОРТИРОВКА ---------------------- */

// Меняет местами два числа
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

// Разделяет массив относительно опорного элемента
int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // Берем последний элемент как опорный
    int i = low - 1;        // Индекс меньших элементов

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);  // Ставим опорный элемент на место
    return i + 1;
}

// Рекурсивная функция быстрой сортировки
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);   // Сортируем левую часть
        quickSort(arr, pi + 1, high);  // Сортируем правую
    }
}

/* ---------------------- СОРТИРОВКА СЛИЯНИЕМ ---------------------- */

// Объединяет две отсортированные части массива
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }

    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

// Рекурсивно делит массив и вызывает слияние
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

/* ---------------------- ИНТЕРПОЛЯЦИОННЫЙ ПОИСК ---------------------- */

// Возвращает индекс найденного элемента или -1, если его нет
int interpolationSearch(int arr[], int n, int x) {
    int low = 0, high = n - 1;

    while (low <= high && x >= arr[low] && x <= arr[high]) {
        if (arr[low] == arr[high]) {
            if (arr[low] == x) return low;
            return -1;
        }

        // Формула вычисления предполагаемой позиции
        int pos = low + ((double)(high - low) / (arr[high] - arr[low])) * (x - arr[low]);

        if (arr[pos] == x) return pos;
        if (arr[pos] < x) low = pos + 1;
        else high = pos - 1;
    }

    return -1;
}

/* ---------------------- ОСНОВНАЯ ПРОГРАММА ---------------------- */

int main() {
    // Тест для быстрой сортировки
    int arr1[] = {10, 7, 8, 9, 1, 5};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);

    cout << "Исходный массив (быстрая сортировка): ";
    for (int x : arr1) cout << x << " ";
    cout << endl;

    quickSort(arr1, 0, n1 - 1);

    cout << "После быстрой сортировки: ";
    for (int x : arr1) cout << x << " ";
    cout << "\n\n";


    // Тест для сортировки слиянием
    int arr2[] = {38, 27, 43, 3, 9, 82, 10};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);

    cout << "Исходный массив (сортировка слиянием): ";
    for (int x : arr2) cout << x << " ";
    cout << endl;

    mergeSort(arr2, 0, n2 - 1);

    cout << "После сортировки слиянием: ";
    for (int x : arr2) cout << x << " ";
    cout << "\n\n";


    // Тест для интерполяционного поиска
    int sortedArr[] = {10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47};
    int n3 = sizeof(sortedArr) / sizeof(sortedArr[0]);
    int target = 18;

    int index = interpolationSearch(sortedArr, n3, target);

    cout << "Интерполяционный поиск числа " << target << ": ";
    if (index != -1) cout << "найдено на позиции " << index << endl;
    else cout << "не найдено" << endl;

    return 0;
}
