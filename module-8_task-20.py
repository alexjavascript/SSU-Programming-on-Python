import numpy as np
import random

a = np.zeros((12,3))

for i in range(0, 12):
    for j in range(0, 3):
        a[i][j] = np.floor(random.random() * 10)
        
        
print(a)
print()

print(a[9,1])
print()

print(a[:,1])
print()

print(a[-2::-2, 0])
print()

a = np.reshape(a, (6,6))
print(a)
print()

''' n = int(input("Введите степень n: ")) '''
a = a**2
print(a)
print()

for i in range(0, 6):
  print(np.min(a[:,i]))
print()

print(np.max(a[5]))
print()

n = 10 
'''int(input("Введите кол-во элементов n в массиве b: ")) '''
b = np.zeros(n)

for i in range(0, n):
  b[i] = np.floor(random.random() * 200 - 100)
print(b)
print()

isNegativeSequence = False
for i in range(0, n - 1):
  if ( (b[i] < 0) and (b[i+1] < 0) ):
    isNegativeSequence = True
    break

if (isNegativeSequence):
  print("Имеется последовательность с 2 отрицательными подряд значениями") 
else:
  print("Не имеется последовательность с 2 отрицательными подряд значениями")
print() 

print(a)
print(a[].size)
c = np.array(0)
for i in range(0, a[].size):
  minValue = np.min(a[i])
  print(minValue)
  minIndex = np.where(a[i] == minValue)  
  minIndex = minIndex[0][0]
  print('1', minIndex)

  vectorRight = np.array(0)
  vectorRight = a[minIndex:]
  np.append(c, vectorRight)

  print('end iter',i)

print(c)
