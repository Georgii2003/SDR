import numpy as np
import matplotlib.pyplot as plt

# Создаем данные для графиков
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 8))

# Создаем график в виде отсчетов
a1.stem(x, y, linefmt='b-', markerfmt='bo', basefmt='r-')
a1.set_xlabel('X')
a1.set_ylabel('Y')
a1.set_title('График в виде отсчетов')
a1.grid(True)

# Создаем график в виде квантованных уровней
a2.step(x, y, 'r-', where='post')
a2.set_xlabel('X')
a2.set_ylabel('Y')
a2.set_title('График в виде квантованных уровней')
a2.grid(True)

plt.tight_layout()
plt.show()