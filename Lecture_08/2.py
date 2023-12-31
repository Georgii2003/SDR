import numpy as np   
import matplotlib.pyplot as plt  
from scipy.fftpack import fft, ifft,  fftshift, ifftshift 
from scipy import signal
from scipy.signal import max_len_seq

# Create radio 
sdr = adi.Pluto("ip:192.168.2.1") 
 
# Configure properties 
sdr.rx_lo = 2452000000
sdr.tx_lo = 2452000000

ft = 100e3 # частота следования символов
fs = 600e3
ns = fs/ft

data=max_len_seq(5)[0]
#Преобразование нулей и единиц последовательности в передаваемое сообщение
m=2*data-1
ts1 =np.array([0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1])
ts1t = 2*ts1-1
b = np.ones(int(ns)) #Коэффициенты фильтра интерполятора
#x_IQ = np.hstack((ts1t,m)) # формирование пакета
x_IQ = m # формирование пакета 
 
N_input = len(x_IQ)
xup = np.hstack((x_IQ.reshape(N_input,1),np.zeros((N_input, int(ns-1)))))
xup= xup.flatten()
x1 = signal.lfilter(b, 1,xup)
x=x1.astype(complex)  
xt=.5*(1+x) #комплексные отсчеты для adalm

triq=2**14*xt
n_frame= len(triq)
sdr.tx(triq)

sdr.rx_rf_bandwidth = 200000
sdr.rx_destroy_buffer()
sdr.tx_hardwaregain_chan0 = -10
sdr.rx_buffer_size = 2*n_frame
xrec1=sdr.rx()
xrec = xrec1/np.mean(xrec1**2)

