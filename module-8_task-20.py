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

n = int(input("Введите степень n: "))
a = a**n
