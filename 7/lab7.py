# Входные данные
universe = set(range(1, 11))  # {1,2,...,10}
subsets = {
    "S1": {1, 2, 3},
    "S2": {2, 4, 6},
    "S3": {3, 5, 7},
    "S4": {1, 4, 7, 10},
    "S5": {5, 6, 8, 9},
}

def greedy_set_cover(universe, subsets):
    uncovered = set(universe)           # элементы, которые ещё не покрыты
    chosen_sets = []                    # список имён выбранных множеств в порядке выбора
    covered_elements = set()            # объединение выбранных множеств

    # пока есть непокрытые элементы, выбираем множество, покрывающее
    # максимальное число ещё непокрытых элементов
    while uncovered:
        best_set_name = None
        best_set_cover_size = 0
        best_set_elements = None

        # перебираем все множества и считаем, сколько новых (ещё непокрытых) элементов они дают
        for name, s in subsets.items():
            new_elements = s & uncovered   # пересечение: элементы этого множества, которые ещё не покрыты
            new_count = len(new_elements)
            if new_count > best_set_cover_size:
                best_set_cover_size = new_count
                best_set_name = name
                best_set_elements = new_elements

        # если ни одно множество не добавляет новых элементов — дальнейшее покрытие невозможно
        if best_set_name is None or best_set_cover_size == 0:
            break

        # выбираем лучшее множество: помечаем его выбранным, обновляем покрытие и множество непокрытых
        chosen_sets.append(best_set_name)
        covered_elements.update(subsets[best_set_name])
        uncovered -= best_set_elements

        # можно (но не обязательно) удалять выбранное множество из candidates, чтобы не смотреть на него снова:
        # del subsets[best_set_name]

    return chosen_sets, covered_elements

chosen, covered = greedy_set_cover(universe, dict(subsets))
print("Выбранные множества (в порядке выбора):", chosen)
print("Общее количество элементов в объединении выбранных множеств:", len(covered))
print("Объединение выбранных множеств:", covered)
