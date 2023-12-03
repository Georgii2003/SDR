import numpy as np 
import random
array = np.random.randint(-1000, 1000, size = 1024)
array.sort()
for i in array:
    if i > 0:
     print(i)