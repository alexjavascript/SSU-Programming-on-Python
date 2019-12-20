###### Саратовской государственный университет им. Чернышевского
###### 4 курс | 2019

# Спец. курс "Программирование на Python"
"Programming on Python" — course practice at the Saratov State University.

**Преподаватель по теоретической и практической частям:** [Крусс Юлия Сергеевна](https://www.sgu.ru/person/kruss-yuliya-sergeevna)



## Блок 0 | Простые алгоритмы
### Задание 1
#### Номер 5

Дано число n. Напечатать те натуральные числа, квадрат которых не превышает n.

```
n = int(input("Enter N >> "))
i = 0
while (i * i <= n):
  print(i)
  i = i + 1
```

### Задание 2
#### Номер 5

Дан целочисленный массив размера N. Вывести вначале все содержащиеся в данном массиве четные числа в порядке возрастания их индексов, а затем — все нечетные числа в порядке убывания их индексов.  

```
n = int(input("Enter N >> "))
a = []

i = 0
while (i < n):
  buff = int(input("Enter your value >> "))
  a.append(buff)
  i = i + 1

b = []
i = 0
while(i < n):
  if (a[i] % 2 == 0):
    b.append(a[i])
  i = i + 1

i = 0
while(i < n):
  if (a[i] % 2 != 0):
    b.append(a[i])
  i = i + 1

i = 0;
while (i < n):
  print(b[i])
  i = i + 1
```

### Задание 3
#### Номер 15

Дан массив размера N. Найти номер его первого локального минимума (локальный минимум — это элемент, который меньше любого из своих соседей).

```
n = int(input("Enter N >> "))
a = []

i = 0
while (i < n):
  buff = int(input("Enter your value >> "))
  a.append(buff)
  i = i + 1

i = 1;
while (i < n - 1):
  if (a[i] < a[i - 1] and a[i] < a[i + 1]):
    print("Local minimum is a[", i, "] = ", a[i])
  i = i + 1
```

### Задание 4
#### Номер 5

Дана целочисленная матрица размера M × N. Найти количество ее столбцов, все элементы которых различны.

```
n = int(input("Enter N >> "))
m = int(input("Enter M >> "))
result = 0

a = []
i = 0
while (i < n):
  b = []
  j = 0
  while (j < m):
    buff = int(input("Enter your value >> "))
    b.append(buff)
    j = j + 1
  a.append(b)
  i = i + 1
  
i = 0
while (i < m):
  b = []
  j = 0
  while (j < n):
    b.append(a[j][i])
    j = j + 1
  allDifferent = True
  b.sort()
  j = 0
  while (j < n - 1):
    if (b[j] == b[j + 1]):
      allDifferent = False
      print("NOT ALL DIFFERENT", end=" ")
      break
    j = j + 1
  print(b)
  if (allDifferent):
    result = result + 1
    print("ALL DIFFERENT", b)
  i = i + 1

i = 0
while (i < n):
  j = 0
  while (j < m):
    print(a[i][j], end = " ")
    j = j + 1
  print()
  i = i + 1

print("Quantity of Columns which Elements All Different is : ", result)
```



## Блок 8 | Numpy
### Задание 1
#### Номер 15

1. Сгенерировать матрицу размером 12*3, заполненную целыми числами.
2. Вывести на экран элемент с индексами [9,1].
3. Вывести на экран 2 столбец матрицы.
4. Вывести на экран каждый второй элемент 1 столбца матрицы в
обратном порядке
5. Изменить форму матрицы с 12*3 на 6*6.
6. Возвести каждый элемент матрицы в заданную степень
7. Найти минимум в каждом столбце
8. Найти максимальный элемент в последней строке
9. Дан одномерный массив числовых значений, насчитывающий N
элементов. Определить имеются ли в массиве два подряд идущих
отрицательных числа.
10. Дана матрица. В каждой строке найти первый минимальный элемент.
Сформировать вектор из элементов строк, расположенных справа от
минимального (для каждой строки свой минимум)

```
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

# 6
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

```


## Блок 9 | Matplotlib
### Задание 1
#### Номер 5

```
import math
import pylab
from matplotlib import mlab

def func (x):
    return x**(1 / 5)

xmin = 1.0
xmax = 32.0

dx = 0.01

# !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = mlab.frange(xmin, xmax, dx)

# Вычислим значение функции в заданных точках
ylist = [func (x) for x in xlist]

# !!! Нарисуем одномерный график
pylab.plot(xlist, ylist)

# !!! Покажем окно с нарисованным графиком
pylab.show()
```

### Задание 2
#### Номер 15

```
import math
import pylab
from matplotlib import mlab

def func (x):
    return x**(1 / 5)

xmin = 1.0
xmax = 32.0

dx = 0.01

# !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = mlab.frange(xmin, xmax, dx)

# Вычислим значение функции в заданных точках
ylist = [func (x) for x in xlist]

# !!! Нарисуем одномерный график
pylab.plot(xlist, ylist, "-.b")

# !!! Покажем окно с нарисованным графиком
pylab.show()
```

### Задание 3
#### Номер 15

```
import math
import pylab
from matplotlib import mlab

def func_1 (x):
    return x**(1 / 5)

def func_2 (x):
    return (- 1 * x**(1 / 5))

def func_3 (x):
    return (2 * x**(1 / 5))

xmin = 1.0
xmax = 32.0

dx = 0.01

xlist = mlab.frange(xmin, xmax, dx)
ylist_1 = [func_1 (x) for x in xlist]
ylist_2 = [func_2 (x) for x in xlist]
ylist_3 = [func_3 (x) for x in xlist]

pylab.plot(xlist, ylist_1, "-.b", label="f(x)")
pylab.plot(xlist, ylist_2, "-.r", label="-1 * f(x)")
pylab.plot(xlist, ylist_3, "-.g", label="2 * f(x)")

pylab.grid()
pylab.legend(loc='upper right') 
pylab.show()
```

### Задание 4
#### Номер 15

```
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy


def makeData ():
    x = numpy.arange (-3, 3, 0.1)
    y = numpy.arange (-3, 3, 0.1)
    
    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid = numpy.sqrt( xgrid**2 + ygrid**2 )
    
    return xgrid, ygrid, zgrid


x, y, z = makeData()

fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, z)
pylab.show()
```

![Figure_1](https://user-images.githubusercontent.com/20648009/70770292-b511d000-1d64-11ea-9795-b87d25714a85.png)


```
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt


def makeData ():
    x = numpy.arange (-3, 3, 0.1)
    y = numpy.arange (-3, 3, 0.1)
    
    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid = numpy.sqrt( xgrid**2 + ygrid**2 )
    
    return xgrid, ygrid, zgrid


x, y, z = makeData()

fig = pylab.figure()

cs = plt.contourf(x, y, z, 100)

plt.colorbar(cs)
plt.show()
```

![Figure_1-1](https://user-images.githubusercontent.com/20648009/70772546-c65eda80-1d6c-11ea-8515-fc9913edbd0e.png)


