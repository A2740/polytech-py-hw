import numpy as np
import pandas as pd

# 1. Различные способы создания объектов типа Series
print(f"{'Задание №1':-^40}")

# Создание Series из списка
print("Series из списка:")
values = [10, 20, 30, 40, 50]
series_list = pd.Series(values)
print(series_list)

# Создание Series из массива NumPy
print("\nSeries из массива NumPy:")
np_array = np.array([5, 15, 25, 35, 45])
series_np = pd.Series(np_array)
print(series_np)

# Создание Series из скалярного значения
print("\nSeries из скаляра:")
scalar_value = 99
series_scalar = pd.Series(scalar_value, index=[0, 1, 2, 3])
print(series_scalar)

# Создание Series из словаря
print("\nSeries из словаря:")
data_dict = {'x': 100, 'y': 200, 'z': 300}
series_dict = pd.Series(data_dict)
print(series_dict)

# 2. Различные способы создания объектов типа DataFrame
print(f"{'Задание №2':-^40}")

# Создание DataFrame из списка словарей
print("\nDataFrame из списка словарей:")
list_of_dicts = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]
df_list_dicts = pd.DataFrame(list_of_dicts)
print(df_list_dicts)

# Создание DataFrame из словаря списков
print("\nDataFrame из словаря списков:")
dict_of_lists = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df_dict_lists = pd.DataFrame(dict_of_lists)
print(df_dict_lists)

# Создание DataFrame из двумерного массива NumPy
print("\nDataFrame из массива NumPy:")
np_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_np_matrix = pd.DataFrame(np_matrix, columns=['A', 'B', 'C'])
print(df_np_matrix)

# 3. Объединение двух Series с заменой NaN на 1
print(f"{'Задание №3':-^40}")

scores_math = pd.Series({'Alice': 90, 'Bob': 85, 'Charlie': 95})
scores_science = pd.Series({'Alice': 88, 'Bob': 92, 'David': 89})

combined_scores = pd.DataFrame({'Math': scores_math, 'Science': scores_science}).fillna(1)
print(combined_scores)

# 4. Вычитание по столбцам в DataFrame
print(f"{'Задание №4':-^40}")

random_data = np.random.randint(1, 10, (3, 4))
df_random = pd.DataFrame(random_data, columns=['W', 'X', 'Y', 'Z'])
print(df_random.sub(df_random['W'], axis=0))

# 5. Использование методов ffill() и bfill()
print(f"{'Задание №5':-^40}")

df_missing = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 2, np.nan, 4, np.nan],
    'C': [1, 2, np.nan, np.nan, 5]
})
print(df_missing)

print("\nПрименение ffill():")
df_ffilled = df_missing.ffill()
print(df_ffilled)

print("\nПрименение bfill():")
df_bfilled = df_missing.bfill()
print(df_bfilled)
