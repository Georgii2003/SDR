import time  
import adi  
import numpy as np  
import matplotlib.pyplot as plt  
    
sdr = adi.Pluto("ip:192.168.2.1")  
table = 8  
sdr.rx_lo = 2452000000 + 2000000 * table
sdr.tx_lo = 2452000000 + 2000000 * table
sdr.sample_rate = 1e6  
sdr.rx_rf_bandwidth = sdr.sample_rate
sdr.rx_buffer_size = 10000  
sdr.tx_hardwaregain_chan0 = -30 #рекомендуемое значение от 0 до -50

#Генерируем QPSK-модулированный сигнал, 16 сэмплов на символ
num_symbols = 1000
x_int = np.random.randint(0, 4, num_symbols) # 0 to 3
x_degrees = x_int * 360/4.0 + 45 # 45, 135, 225, 315 град.
x_radians = x_degrees * np.pi/180.0 # sin() и cos() в рад.
x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians) #генерируем комплексные числа
samples = np.repeat(x_symbols, 16) # 16 сэмплов на символ
samples *= 2**14 #Повысим значения для наших сэмплов

#destroy buffer
sdr.tx_destroy_buffer()

# Start the transmitter
sdr.tx_cyclic_buffer = True # Enable cyclic buffers
sdr.tx(samples)
rx = sdr.rx

plt.figure(1)
plt.scatter(rx.real, rx.imag)

plt.figure(2)
plt.plot(rx.real, rx.imag)

plt.show()

