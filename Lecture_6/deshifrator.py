bits = (24, [])
array = abs(sdr.rx())
#plt.plot(array)
#plt.show()
count = 0
print("!!!")
for i in range (len(array)):
    if array[i] > 1500:
    	count += 1
    elif array[i] < 500:
    	count = 0
    if(count == 16*100):
    	print("URAAAAAAAAAAAAAAA")
    	count = 0
    	print("index sync end = ", i)
    	array2 = array[(i- 16*100 - 1):i+2000]
    	print(len(array2))
    	plt.plot(array2)
    	plt.show()
    	time.sleep(100)
    	
print(bits)