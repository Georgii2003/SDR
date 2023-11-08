from scipy.fftpack import fft, ifft,  fftshift, ifftshift
import numpy as np
import matplotlib.pyplot as plt

fc1 = 20 # Частота косинуса 
fc2 = 40 # Частота 2 косинуса
fs = 400 # Частота дискретизации
ts = 1/fs
t = np.arange(0, 3, 0.001) # длительность сигнала 
xt = np.cos(2*np.pi*fc1*t)# формирование временного сигнала
'''
Рассчёт значения аналоговой частоты, которая соответствует нормированной 
частоте Ω = 0.1Pi рад, Ω = 0.3Pi рад
'''
fc1_math = (0.1*np.pi*fs)/(2*np.pi)
fc2_math = (0.3*np.pi*fs)/(2*np.pi)
print("Для Ω = 0.1Pi - ", fc1_math, " и для Ω = 0.3Pi - ", fc2_math)

plt.figure(1) 
plt.plot(t,xt)
plt.xlabel('Время (c)')
plt.title('Исходный сигнал')

xn1 = np.arange(0, 64, 1)
xn2 = np.arange(0, 128, 1)
xn3 = np.arange(0, 256, 1)
xd1 = np.cos(2 * np.pi * fc1 * xn1 * ts)
xd2 = np.cos(2 * np.pi * fc1 * xn2 * ts)
xd3 = np.cos(2 * np.pi * fc1 * xn3 * ts)

fig2 = plt.figure(2, figsize=(12, 10))
fig2.suptitle('Дискретизированный сигнал')
plt.subplot(1, 3, 1)
plt.xlabel('Кол-во отсчётов')
plt.title('n = 64')
plt.stem(xn1, xd1)

plt.subplot(1, 3, 2)
plt.xlabel('Кол-во отсчётов')
plt.title('n = 128')
plt.stem(xn2, xd2)

plt.subplot(1, 3, 3)
plt.xlabel('Кол-во отсчётов')
plt.title('n = 256')
plt.stem(xn3, xd3)
'''
Построение модуля спектра для дискретных сигналов с 
n = 64, 128, 256
'''
spectr1 = abs(np.fft.fft(xd1))
spectr2 = abs(np.fft.fft(xd2))
spectr3 = abs(np.fft.fft(xd3))
fsp1 = np.arange(-len(spectr1)/2, len(spectr1)/2, 1) * fs/64
fsp2 = np.arange(-len(spectr2)/2, len(spectr2)/2, 1) * fs/128
fsp3 = np.arange(-len(spectr3)/2, len(spectr3)/2, 1) * fs/256

fig3 = plt.figure(3, figsize=(12, 10))
fig3.suptitle('Модули спектра дискретных сигналов')
plt.subplot(1, 3, 1)
plt.stem(fsp1, spectr1)
plt.title('n = 64')
plt.xlabel('Частота (Гц)')
plt.subplot(1, 3, 2)
plt.stem(fsp2, spectr2)
plt.title('n = 128')
plt.xlabel('Частота (Гц)')
plt.subplot(1, 3, 3)
plt.xlabel('Частота (Гц)')
plt.title('n = 256')
plt.stem(fsp3, spectr3)

signal = np.cos(2*np.pi*fc1*t) + np.cos(2*np.pi*fc2*t)

