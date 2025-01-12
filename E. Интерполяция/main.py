# Функция для генерации признаков многочлена второй степени
def generate_polynomial_features(X):
    n_samples = len(X)
    n_features = len(X[0])
    features = [[1] for _ in range(n_samples)]  # Свободный член (константа)

    # Линейные члены
    for i in range(n_features):
        for j in range(n_samples):
            features[j].append(X[j][i])

    # Квадратичные члены и произведения переменных
    for i in range(n_features):
        for j in range(i, n_features):
            for k in range(n_samples):
                features[k].append(X[k][i] * X[k][j])

    return features

# Решение системы линейных уравнений методом наименьших квадратов
def least_squares(X, y):
    # X_T * X
    XT = transpose(X)
    XTX = matmul(XT, X)

    # X_T * y
    XTy = matvecmul(XT, y)

    # Решение системы XTX * coefficients = XTy
    coefficients = solve_linear_system(XTX, XTy)
    return coefficients

# Транспонирование матрицы
def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Умножение двух матриц
def matmul(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Умножение матрицы на вектор
def matvecmul(A, b):
    result = [0 for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i] += A[i][j] * b[j]
    return result

# Решение системы линейных уравнений (метод Гаусса)
def solve_linear_system(A, b):
    n = len(A)
    # Прямой ход
    for i in range(n):
        # Нормализация строки
        factor = A[i][i]
        for j in range(i, n):
            A[i][j] /= factor
        b[i] /= factor

        # Обнуление столбца
        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]

    # Обратный ход
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))
    return x

# Чтение данных из стандартного ввода
import sys
lines = sys.stdin.read().strip().split("\n")

# Разделение данных на тренировочные и тестовые
train_lines = lines[:1000]
test_lines = lines[1000:]

# Парсинг тренировочных данных
train_data = [[float(x) for x in line.split('\t')] for line in train_lines]
X_train = [row[:-1] for row in train_data]
y_train = [row[-1] for row in train_data]

# Парсинг тестовых данных
test_data = [[float(x) for x in line.split('\t')] for line in test_lines]
X_test = test_data

# Генерация полиномиальных признаков
X_train_poly = generate_polynomial_features(X_train)
X_test_poly = generate_polynomial_features(X_test)

# Метод наименьших квадратов: вычисление коэффициентов
coefficients = least_squares(X_train_poly, y_train)

# Предсказание значений для тестовых точек
y_test_pred = [sum(c * x for c, x in zip(coefficients, row)) for row in X_test_poly]

# Запись результатов в стандартный вывод
for value in y_test_pred:
    print(value)