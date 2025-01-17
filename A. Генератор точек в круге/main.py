# Функция классификации набора точек
def classify_points(points):
    # Вычисляем радиусы точек
    radii = [(x ** 2 + y ** 2) ** 0.5 for x, y in points]
    # Считаем средний радиус
    mean_radius = sum(radii) / len(radii)
    # Для генератора 1 средний радиус ближе к 0.5, для генератора 2 ближе к 0.707
    return 1 if mean_radius < 0.6 else 2


# Функция чтения данных
def read_input():
    datasets = []
    # Считываем 100 строк
    with open("input.txt", "r") as file:
        for line in file:  # Читаем построчно из файла
            line = line.strip()
            nums = list(map(float, line.split()))  # Преобразуем в список чисел
            points = [(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]  # Формируем список точек (x, y)
            datasets.append(points)
    return datasets


# Основная программа
def main():
    # Чтение входных данных
    datasets = read_input()

    # Список для хранения результатов
    results = []

    # Классификация каждого набора
    for points in datasets:
        result = classify_points(points)
        results.append(result)

    # Вывод результатов в консоль
    for res in results:
        print(res)


if __name__ == "__main__":
    main()