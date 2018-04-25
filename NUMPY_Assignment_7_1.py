# Write a function to find moving average in an array over a window:
# Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.
# the moving average sequence is n-k+1=len(array)-3+1 values.

import numpy as np
arr=np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
print('\n')
print('Given Array: ',arr)
print('\n')
window=3
N=len(arr)-window+1		### Total Sequence or moving iteration

print('-'*20)
print('Approach-1 ')
print('-'*20)
x=np.sum(np.array([arr[i:window+i] for i in range(N)]),axis=1) / window		### Using array slicing and sum function in numpy
for i in x:
	print(round(i,2))
	

print('-'*20)
print('Approach-2 ')
print('-'*20)
for i in range(N):						### Using simple for loop and index element from Array
	val=0
	for j in range(i,window+i):
		val=val+arr[j]
		
	print(round(val/window,2))
