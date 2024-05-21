import matplotlib.pyplot as plt

# Открытие и чтение данных
with open('error_probability.txt', 'r') as file:
    lines = file.readlines()

# Разделение данных
std_devs = []
error_probabilities = []
for line in lines:
    std_dev, error_probability = line.split()
    std_devs.append(float(std_dev))
    error_probabilities.append(float(error_probability))

# Вывод графика
plt.figure(figsize=(10, 6))
plt.plot(std_devs, error_probabilities, marker='o')
plt.title('Зависимость вероятности ошибки на бит от дисперсии шума')
plt.xlabel('Дисперсия шума')
plt.ylabel('Вероятность ошибки на бит')
plt.grid(True)
plt.show()
