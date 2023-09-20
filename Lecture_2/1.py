import time
import timeit
import numpy as np
import matplotlib.pyplot as plt

python_sort_times = []
numpy_sort_times = []


n_values = list(range(10, 5000001, 100000))

for n in n_values:
    # Генерируем случайный список из n элементов
    random_list = np.random.randint(0, 1000, n).tolist()
    
    # Измеряем время выполнения сортировки для Python List
    python_time = timeit.timeit(lambda: sorted(random_list), number=1)
    python_sort_times.append(python_time)
    
    # Измеряем время выполнения сортировки для NumPy
    numpy_time = timeit.timeit()
    numpy_sort_times.append(numpy_time)

# Строим график

plt.figure(figsize=(10, 6)) 
plt.plot(n_values, python_sort_times, label='Python List Sort', color='b') 
plt.plot(n_values, numpy_sort_times, label='NumPy Sort', color='r') 
plt.xlabel('Количество элементов') 
plt.ylabel('Время выполнения (секунды)') 
plt.title('Сравнение времени выполнения сортировки') 
plt.legend() 
plt.grid(True)
plt.show()