# -*- coding: utf-8 -*-

from scipy.fftpack import fft, ifft,  fftshift, ifftshift
import numpy as np
import matplotlib.pyplot as plt

fc=10 # Частота косинуса 
fs=32*fc # частота дискретизации, избыточная 
t=np.arange( 0, 2,  1/fs) # длительность сигнала 2 с
x=np.cos(2*np.pi*fc*t) # формирование временного сигнала



plt.figure(1)
plt.plot(t,x) 
plt.stem(t,x) # для отображения временных отсчетов сигнала, выбрать длительность 0.2 сек
plt.xlabel('$t=nT_s$')
plt.ylabel('$x[n]$')

fc1=20 # Частота косинуса 
fs1=32*fc # частота дискретизации, избыточная 
t1=np.arange( 0, 2,  1/fs1) # длительность сигнала 2 с
x1=np.cos(2*np.pi*fc1*t1) # формирование временного сигнала

plt.figure(2)
plt.plot(t1,x1) 
plt.stem(t1,x1) # для отображения временных отсчетов сигнала, выбрать длительность 0.2 сек
plt.xlabel('$t=nT_s$')
plt.ylabel('$x[n]$')

