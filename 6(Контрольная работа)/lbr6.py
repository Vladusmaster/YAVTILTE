# Блочная (корзинная) сортировка
def bucket_sort(arr):
    # Проверяем, не пуст ли массив
    if len(arr) == 0:
        return arr

    # Находим минимальное и максимальное значения
    min_val, max_val = min(arr), max(arr)

    # Количество корзин (по количеству элементов)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Распределяем элементы по корзинам
    for num in arr:
        index = int((num - min_val) / (max_val - min_val + 1e-9) * (bucket_count - 1))
        buckets[index].append(num)

    # Сортируем каждую корзину и объединяем
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr


# Проверка
data = [0.78, 0.12, 0.23, 0.9, 0.56, 0.44]
print("Исходный массив блочной сортировки:", data)
print("Отсортированный массив блочной сортировки:", bucket_sort(data))

# Блинная сортировка
def flip(arr, k):
    arr[:k+1] = reversed(arr[:k+1])

def pancake_sort(arr):
    n = len(arr)
    for size in range(n, 1, -1):
        # Находим индекс максимального элемента
        max_index = arr.index(max(arr[:size]))
        if max_index != size - 1:
            # Переворачиваем, чтобы максимум стал первым
            flip(arr, max_index)
            # Переворачиваем снова, чтобы максимум оказался в конце
            flip(arr, size - 1)
    return arr

# Проверка
data = [3, 6, 1, 10, 2, 8]
print("Исходный массив блинной сортировки:", data)
print("Отсортированный массив блинной сортировки:", pancake_sort(data))

# Сортировка бусинами (гравитационная)
def bead_sort(arr):
    # Алгоритм работает только с неотрицательными числами
    if any(x < 0 for x in arr):
        raise ValueError("Алгоритм работает только с неотрицательными числами")

    max_num = max(arr)

    # Формируем сетку (матрицу), где каждая строка — это бусины числа
    # 1 — бусина, 0 — пустое место
    grid = [[1] * num + [0] * (max_num - num) for num in arr]

    # Имитируем "гравитацию": бусины падают вниз по каждому столбцу
    for j in range(max_num):
        # Считаем количество бусин в каждом столбце
        beads = sum(row[j] for row in grid)
        # Заполняем столбец заново: бусины "оседают" внизу
        for i in range(len(arr)):
            grid[i][j] = 1 if i >= len(arr) - beads else 0

    # Подсчитываем количество бусин в каждой строке — это и есть отсортированные значения
    result = [sum(row) for row in grid]
    return result

# Проверка
data = [5, 3, 1, 7, 4]
print("Исходный массив сортировки бусинами:", data)
print("Отсортированный массив сортировки бусинами:", bead_sort(data))

# Поиск скачками (Jump Search)
import math


def jump_search(arr, target):
    n = len(arr)
    # Размер "шага" — обычно корень из длины массива
    step = int(math.sqrt(n))
    prev = 0

    # Прыгаем по массиву с шагом, пока элемент меньше искомого
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # элемент не найден

    # Когда диапазон найден — делаем линейный поиск в этом блоке
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i  # возвращаем индекс найденного элемента
    return -1  # если не нашли

# Проверка
data = [1, 3, 5, 7, 9, 11, 13]
x = 9
print("Массив поиска скачками:", data)
print("Искомое значение поиска скачками:", x)
print("Результат поиска скачками:", jump_search(data, x))

# Экспоненциальный поиск (Exponential Search)
def binary_search(arr, left, right, target):
    # Классический бинарный поиск на диапазоне [left, right]
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # не найден

def exponential_search(arr, target):
    # Проверяем первый элемент отдельно
    if arr[0] == target:
        return 0

    # Расширяем диапазон экспоненциально: 1, 2, 4, 8, 16...
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    return binary_search(arr, i // 2, min(i, len(arr) - 1), target)

# Проверка
data = [2, 4, 6, 8, 10, 12, 14, 16]
x = 10
print("Массив экспоненциального поиска:", data)
print("Искомое значение экспоненциального поиска:", x)
print("Результат экспоненциального поиска:", exponential_search(data, x))

#Тернарный поиск (Ternary Search)
def ternary_search(arr, target, left, right):
    # Проверяем, не вышли ли за границы
    if right >= left:
        # Делим диапазон на три части
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Проверяем, не совпал ли элемент с одной из границ
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        # Если искомое значение меньше — ищем в первой трети
        if target < arr[mid1]:
            return ternary_search(arr, target, left, mid1 - 1)
        # Если больше — ищем в последней трети
        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2 + 1, right)
        # Иначе — в средней трети
        else:
            return ternary_search(arr, target, mid1 + 1, mid2 - 1)

    return -1  # элемент не найден

# Проверка
data = [1, 2, 4, 5, 7, 9, 11]
x = 9
print("Массив тернарного поиска:", data)
print("Искомое значение тернарного поиска:", x)
print("Результат тернарного поиска:", ternary_search(data, x, 0, len(data) - 1))





