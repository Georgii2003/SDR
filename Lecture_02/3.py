import timeit
import numpy as np
import matplotlib.pyplot as plt

python_sort_times = []
numpy_sort_times = []

fig, (a1, a2, a3) = plt.subplots(3, 1, figsize=(8, 8))

n_values = list(range(10, 5000001, 100000))

for n in n_values:
    # Генерируем случайный список из n элементов
    random_list = np.random.randint(0, 1000, n).tolist()
    
    # Измеряем время выполнения сортировки для Python List
    python_time = timeit.timeit(lambda: sorted(random_list), number=1)
    python_sort_times.append(python_time)
    
    # Измеряем время выполнения сортировки для NumPy
    numpy_time = timeit.timeit(lambda: np.sort(random_list, kind='quicksort'), number=1)
    numpy_sort_times.append(numpy_time)

# Создаем график в виде отсчетов
a1.stem(n_values, python_sort_times, linefmt='b-', markerfmt='bo', basefmt='r-')
a1.set_xlabel('Количество элементов')
a1.set_ylabel('Время выполнения (секунды)')
a1.set_title('Дискретный')
a1.grid(True)

# Создаем график в виде квантованных уровней
a2.step(n_values, numpy_sort_times, 'r-', where='post')
a2.set_xlabel('Количество элементов')
a2.set_ylabel('Время выполнения (секунды)')
a2.set_title('Квантованный')
a2.grid(True)

# Создаем график сортировок
a3.plot(n_values, python_sort_times, color='b') 
a3.plot(n_values, numpy_sort_times, color='r') 
a3.set_xlabel('Количество элементов') 
a3.set_ylabel('Время выполнения (секунды)') 
a3.set_title('Аналоговый') 
a3.grid(True)

plt.tight_layout()
plt.show()