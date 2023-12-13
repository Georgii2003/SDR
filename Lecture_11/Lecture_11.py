import adi
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.signal import max_len_seq

sdr = adi.Pluto('ip:192.168.3.1')
sdr.sample_rate = 1000000
sdr.tx_destroy_buffer()
 

sdr.rx_lo = 2000000000
sdr.tx_lo = 2000000000
sdr.tx_cyclic_buffer = True
#sdr.tx_cyclic_buffer = False
sdr.tx_hardwaregain_chan0 = -5
sdr.gain_control_mode_chan0 = "slow_attack"


fs = sdr.sample_rate
rs=100000
ns=fs//rs
buffer_size=1000

data=max_len_seq(8)[0] 
data = np.concatenate((data,np.zeros(1)))
 
 
x_ = np.array([1,1,1,-1,-1,-1,1,-1,-1,1,-1])
b7=np.array([1,-1,1,1,1,-1,1])
ts1 =np.array([0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1])
ts2 =[0,0,1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1]
ts3 =[1,0,1,0,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,1,1,1,1]
ts4 =[1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,0]
m=2*data-1
#ts1t=2*ts1-1
ts1t=b7
 

b = np.ones(int(ns))

x=np.reshape(m,(2,128))
xi=x[0,:]
xq=x[1,:]
x_bb=(xi+1j*xq)/np.sqrt(2)
plt.figure(1)
plt.scatter(x_bb.real,x_bb.imag)

xiq=2**14*x_bb
n_frame= len(xiq)
sdr.tx(xiq)

sdr.rx_rf_bandwidth = 10000
sdr.rx_destroy_buffer()
sdr.rx_hardwaregain_chan0 = -5
sdr.rx_buffer_size =2*n_frame
xrec1=sdr.rx()
xrec = xrec1/np.mean(xrec1**2)

rx_symbols = sdr.rx()
rx4 = rx_symbols ** 4
fft_rx4 = np.fft.fft(rx4, n= buffer_size)
arg_max = np.argmax(fft_rx4)
r = np.linspace(-np.pi, np.pi, buffer_size)
plt.figure(2)
plt.plot(abs(fft_rx4))

ph1 = arg_max/4
shift = np.fft.fftshift(fft_rx4)

plt.figure(3)
plt.plot(r,abs(shift))

exp = rx_symbols * np.exp(-1j * ph1)

plt.figure(4)
plt.scatter(exp.real, exp.imag)
plt.figure(5)
plt.plot(x_bb)