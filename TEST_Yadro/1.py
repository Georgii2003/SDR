import time   
import adi   
import numpy as np   
import matplotlib.pyplot as plt  
from scipy.fftpack import fft, ifft,  fftshift, ifftshift 

num_symbols = 100
Ns = 100   
bits = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,   
                 0,1,1,1,0,0,1,1,   
                 0,1,1,0,1,1,1,1,   
                 0,1,1,1,0,0,1,1,  
                 1,1,1,1,1,1,1,1,1,1,1])   
  
                   
sdr = adi.Pluto("ip:192.168.2.1")   
sdr.rx_lo = 900000000 
sdr.tx_lo = 900000000 
sdr.sample_rate = 1e6   
sdr.rx_buffer_size = 10000   
sdr.tx_hardwaregain_chan0 = -30 #рекомендуемое значение от 0 до -50
sdr.rx_rf_bandwidth = sdr.sample_rate 

#Генерируем QPSK-модулированный сигнал
x_int = np.random.randint(0, 4, num_symbols)
qpsk_bits = []
for i in range(len(x_int)):
    if x_int[i] == 0:
        qpsk_bits += '00'
    elif x_int[i] == 1:
        qpsk_bits += '01'
    elif x_int[i] == 2:
        qpsk_bits += '10' 
    else:
        qpsk_bits += '11'

x_degrees = x_int * 360/4.0 + 45
x_radians = x_degrees * np.pi/180.0 
x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians)
samples = np.repeat(x_symbols, 16)
samples *= 2**12 

#destroy buffer
sdr.tx_destroy_buffer()

# Start the transmitter
sdr.tx_cyclic_buffer = True # Enable cyclic buffers
sdr.tx(samples)

print(qpsk_bits)
while 1:
    rx = sdr.rx()
    plt.clf()
    plt.scatter(rx.real,rx.imag)
    plt.draw()

while 1:
    rx = sdr.rx()
    plt.clf()
    plt.plot(rx.real, rx.imag)
    plt.draw()
plt.show()