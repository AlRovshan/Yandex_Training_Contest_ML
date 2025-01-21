def min_statues_cost(n, k, a_i):
    # Инициализация переменных
    min_cost = float('inf')  # Переменная для минимальной стоимости
    current_cost = 0  # Текущая стоимость подотрезка
    types_count = {}  # Счетчик для количества каждого типа в текущем окне

    left = 0  # Левая граница окна

    for right in range(n):
        # Добавляем текущую статуэтку в окно
        if 1 <= a_i[right] <= k:
            types_count[a_i[right]] = types_count.get(a_i[right], 0) + 1
        current_cost += a_i[right]

        # Проверяем, содержит ли окно все виды от 1 до k
        while len(types_count) == k:
            # Обновляем минимальную стоимость
            min_cost = min(min_cost, current_cost)

            # Убираем левую статуэтку из окна
            if 1 <= a_i[left] <= k:
                types_count[a_i[left]] -= 1
                if types_count[a_i[left]] == 0:
                    del types_count[a_i[left]]
            current_cost -= a_i[left]
            left += 1

    return min_cost

# Ввод данных
n, k = map(int, input().split())
a_i = list(map(int, input().split()))

# Вывод результата
print(min_statues_cost(n, k, a_i))