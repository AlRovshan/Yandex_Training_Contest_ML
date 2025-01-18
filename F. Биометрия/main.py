import librosa
import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier

# Путь к тренировочной и тестовой папкам
train_folder = "/content/train/"
test_folder = "/content/test/"
train_targets_path = "/content/train/targets.tsv"

# Функция для извлечения признаков из мел-спектрограммы
def extract_features(file_path, n_mels=128):
    y, sr = librosa.load(file_path, sr=None)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels)
    S_dB = librosa.power_to_db(S, ref=np.max)

    # Вычисляем статистики из спектрограммы
    mean = np.mean(S_dB, axis=1)
    std = np.std(S_dB, axis=1)
    max_val = np.max(S_dB, axis=1)
    min_val = np.min(S_dB, axis=1)

    # Формируем вектор признаков
    features = np.hstack([mean, std, max_val, min_val])
    return features

#Обработка тренировочных данных
train_data = []
train_labels = []

# Читаем файл targets.tsv
train_targets = pd.read_csv(train_targets_path, sep="\t", header=None, names=["file", "gender"])

# Извлекаем признаки из каждого файла
for _, row in train_targets.iterrows():
    file_name, gender = row["file"], row["gender"]
    file_path = os.path.join(train_folder, file_name + '.wav')

    # Извлечение признаков
    features = extract_features(file_path)
    train_data.append(features)
    train_labels.append(gender)

# Преобразуем данные в массивы numpy
X_train = np.array(train_data)
y_train = np.array(train_labels)

# Обучение модели
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Обработка тестовых данных
test_files = os.listdir(test_folder)
test_data = []
test_ids = []

for file_name in test_files:
    if file_name.endswith(".wav"):
        file_path = os.path.join(test_folder, file_name)
        features = extract_features(file_path)
        test_data.append(features)
        test_ids.append(file_name)

# Преобразуем тестовые данные в массив
X_test = np.array(test_data)

# Предсказание пола
y_pred = clf.predict(X_test)

# Формирование файла с ответами
output_path = "/content/targets.txt"
with open(output_path, "w") as f:
    for file_name, gender in zip(test_ids, y_pred):
        file_id = os.path.splitext(file_name)[0]
        f.write(f'"{file_id}\t{gender}"\n')