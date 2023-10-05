import time

import adi
import matplotlib.pyplot as plt
import numpy as np

# Используем элементы библиотеки для вывода
from scipy.fftpack import fft, ifft,  fftshift, ifftshift

# Create radio
sdr = adi.Pluto("ip:192.168.2.1")

# Configure properties
sdr.rx_lo = 2452000000

# Collect data
for r in range(60):
    rx = sdr.rx()
    plt.clf()
    plt.plot(rx.real)
    plt.plot(rx.imag)
    plt.ylim([-2000, 2000])
    plt.draw()
    if rx.imag[10] > 200:
    	time.sleep(5)
    plt.pause(0.05)
    time.sleep(0.1)

# Были добавлены
N=512
X = fft(rx,N)/N
plt.figure("FFT")
plt.stem(abs(X))
    
plt.show()
