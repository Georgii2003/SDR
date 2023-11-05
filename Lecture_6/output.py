import time   
import adi   
import numpy as np   
import matplotlib.pyplot as plt  

     
sdr = adi.Pluto("ip:192.168.2.1")   
table = 8   
sdr.rx_lo = 2000000000 + 2000000 * table   
#sdr.tx_lo = 2000000000 + 2000000 * table   
sdr.sample_rate = 1e6   
sdr.rx_buffer_size = 100000   
#samples = np.ones(sym_length * len(bits), dtype=complex)  


for r in range(1): 
    rx = sdr.rx()    
    #plt.plot(big_array)   
    #plt.plot(rx.imag)  
    plt.clf()  
    plt.plot(abs(rx))    
    plt.draw() 
    plt.pause(0.05) 
    time.sleep(0.1) 
plt.show()