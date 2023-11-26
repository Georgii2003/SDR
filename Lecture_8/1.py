import numpy as np   
import matplotlib.pyplot as plt  
from scipy.fftpack import fft, ifft,  fftshift, ifftshift 

x = np.array([1,1,1,-1,1])
y = (np.correlate(x,x, "full"))
plt.plot(np.abs(y))
plt.show()