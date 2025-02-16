import pandas as pd
import numpy as np

# 1. Использование мультииндексных ключей
index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]

# Создание Series с мультииндексом
pop = pd.Series(population, index=pd.MultiIndex.from_tuples(index, names=['city', 'year']))

# Создание DataFrame
pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)

# Примеры использования .loc с мультииндексом
pop_df_1 = pop_df.loc['city_1', 'something']  # Выбор данных для 'city_1' и столбца 'something'
print("Данные для city_1 и столбца 'something':")
print(pop_df_1)

pop_df_2 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]  # Выбор данных для 'city_1', 'city_3' и столбцов 'total', 'something'
print("\nДанные для city_1, city_3 и столбцов 'total', 'something':")
print(pop_df_2)

pop_df_3 = pop_df.loc[['city_1', 'city_3'], 'something']  # Выбор данных для 'city_1', 'city_3' и столбца 'something'
print("\nДанные для city_1, city_3 и столбца 'something':")
print(pop_df_3)

# 2. Выбор данных по условиям
# Создание мультииндекса и столбцов
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2', 'city_3'],
        [2010, 2020]
    ],
    names=['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

# Создание DataFrame с мультииндексом
data = np.random.randint(1, 100, size=(6, 6))
df = pd.DataFrame(data, index=index, columns=columns)

# Выбор данных:
# - для 2020 года (все столбцы)
df_2020 = df.xs(2020, level='year')
print("\nДанные за 2020 год:")
print(df_2020)

# - для job_1 (все строки)
df_job_1 = df.xs('job_1', level='job', axis=1)
print("\nДанные для job_1:")
print(df_job_1)

# - для city_1 и job_2
df_city_1_job_2 = df.loc['city_1'].xs('job_2', level='job', axis=1)
print("\nДанные для city_1 и job_2:")
print(df_city_1_job_2)

# 3. Использование pd.IndexSlice
idx = pd.IndexSlice

# - все данные по person_1 и person_3
df_person_1_3 = df.loc[:, idx[['person_1', 'person_3'], :]]
print("\nДанные по person_1 и person_3:")
print(df_person_1_3)

# - все данные по первому городу и первым двум person-ам (с использованием срезов)
df_city_1_person_1_2 = df.loc['city_1', idx[['person_1', 'person_2'], :]]
print("\nДанные по первому городу и первым двум person-ам:")
print(df_city_1_person_1_2)

# 4. Пример использования inner и outer джойнов для Series
ser1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
ser2 = pd.Series(['b', 'c', 'f'], index=[4, 5, 6])

# Outer join (объединение с сохранением всех элементов)
outer_join = pd.concat([ser1, ser2], join='outer')
print("\nOuter join:")
print(outer_join)

# Inner join (объединение только с общими элементами)
inner_join = pd.concat([ser1, ser2], join='inner')
print("\nInner join:")
print(inner_join)
