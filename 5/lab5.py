# ---------------------- СОРТИРОВКА ВСТАВКАМИ ----------------------

def insertion_sort(arr):
    """Сортировка вставками"""
    for i in range(1, len(arr)):
        key = arr[i]         # Текущий элемент
        j = i - 1            # Индекс предыдущего элемента

        # Сдвигаем элементы, пока не найдём место для key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Тест сортировки вставками
arr1 = [12, 11, 13, 5, 6]
print("Исходный массив (вставками):", arr1)
insertion_sort(arr1)
print("После сортировки:", arr1)
print()


# ---------------------- СОРТИРОВКА ШЕЛЛА ----------------------

def shell_sort(arr):
    """Сортировка Шелла"""
    gap = len(arr) // 2  # Начальный шаг

    while gap > 0:
        for i in range(gap, len(arr)):
            current_value = arr[i]
            position = i

            # Сдвигаем элементы, если нарушен порядок
            while position >= gap and arr[position - gap] > current_value:
                arr[position] = arr[position - gap]
                position -= gap
            arr[position] = current_value
        gap //= 2


# Тест сортировки Шелла
arr2 = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив (Шелла):", arr2)
shell_sort(arr2)
print("После сортировки:", arr2)
print()


# ---------------------- БИНАРНЫЙ ПОИСК ----------------------

def binary_search(arr, x):
    """Бинарный поиск элемента x в отсортированном массиве arr"""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid  # Элемент найден

    return -1  # Если элемент не найден


# Тест бинарного поиска
sorted_array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
search_element = 11

print("Массив для бинарного поиска:", sorted_array)
result = binary_search(sorted_array, search_element)
if result != -1:
    print(f"Элемент {search_element} найден на индексе {result}.")
else:
    print(f"Элемент {search_element} не найден.")
print()


# ---------------------- ПОИСК ФИБОНАЧЧИ ----------------------

def fibonacci_search(arr, x):
    """Поиск Фибоначчи"""
    fib_m_minus_2 = 0  # F(m-2)
    fib_m_minus_1 = 1  # F(m-1)
    fib_M = fib_m_minus_1 + fib_m_minus_2  # F(m)

    # Ищем минимальное число Фибоначчи >= длине массива
    while fib_M < len(arr):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_M
        fib_M = fib_m_minus_1 + fib_m_minus_2

    offset = -1  # Смещение начала отрезка

    while fib_M > 1:
        i = min(offset + fib_m_minus_2, len(arr) - 1)

        if arr[i] < x:
            fib_M = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_M - fib_m_minus_1
            offset = i
        elif arr[i] > x:
            fib_M = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_M - fib_m_minus_1
        else:
            return i

    if fib_m_minus_1 and offset + 1 < len(arr) and arr[offset + 1] == x:
        return offset + 1

    return -1


# Тест поиска Фибоначчи
data = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
element_to_find = 85

print("Массив для поиска Фибоначчи:", data)
index = fibonacci_search(data, element_to_find)

if index != -1:
    print(f"Элемент {element_to_find} найден на индексе {index}.")
else:
    print(f"Элемент {element_to_find} не найден.")
