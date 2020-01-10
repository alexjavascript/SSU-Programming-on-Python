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

#### Номер 15

Написать программу, реализующую алгоритм из индивидуального задания
с использованием list, замерить время выполнения и сравнить с готовой
реализацией алгоритма из библиотеки NumPy.

Для более полного анализа проводить сравнения на разных размерностях
входных данных. Например, для матриц можно взять три варианта
реализации: 10х10, 100х100, 500х500. (В зависимости от задания время
выполнения алгоритма на больших размерностях может быть очень
большим, в этом случае размерности можно уменьшить)

Сравнить две матрицы на равенство.

```
import numpy as np
from datetime import datetime

#        
# Comparing time on 
# 10x10 Elements
#

arrNumpyA  = np.random.randint(10, size = [10,10])
arrNumpyB = np.random.randint(10, size = [10,10])

arrListA = arrNumpyA.tolist()
arrListB = arrNumpyB.tolist()

print("10x10 Light Competition is Beginning...")

time = datetime.now()
result = np.array_equal(arrNumpyA, arrNumpyB)
timeNumpy = datetime.now() - time 
print("NumPy Script Time: ", end = " ")
print(time)

time = datetime.now()
result = (arrListA == arrListB)
timeList = datetime.now() - time 
print("List Script Time: ", end = " ")
print(time)

if (timeNumpy > timeList):
    print("NumPy is Winning!")
elif (timeNumpy < timeList):
    print("Lists are Winning! Wooow")
else:
    print("Draw..")

print()
print()

#        
# Comparing time on 
# 100x100 Elements
#

arrNumpyA  = np.random.randint(10, size = [100,100])
arrNumpyB = np.random.randint(10, size = [100,100])

arrListA = arrNumpyA.tolist()
arrListB = arrNumpyB.tolist()

print("100x100 Average Competition is Beginning...")

time = datetime.now()
result = np.array_equal(arrNumpyA, arrNumpyB)
timeNumpy = datetime.now() - time 
print("NumPy Script Time: ", end = " ")
print(time)

time = datetime.now()
result = (arrListA == arrListB)
timeList = datetime.now() - time 
print("List Script Time: ", end = " ")
print(time)

if (timeNumpy > timeList):
    print("NumPy is Winning!")
elif (timeNumpy < timeList):
    print("Lists are Winning! Wooow")
else:
    print("Draw..")

print()
print()

#        
# Comparing time on 
# 500x500 Elements
#

arrNumpyA  = np.random.randint(10, size = [500,500])
arrNumpyB = np.random.randint(10, size = [500,500])

arrListA = arrNumpyA.tolist()
arrListB = arrNumpyB.tolist()

print("500x500 Hard Competition is Beginning... There are much more elements... Oh")

time = datetime.now()
result = np.array_equal(arrNumpyA, arrNumpyB)
timeNumpy = datetime.now() - time 
print("NumPy Script Time: ", end = " ")
print(time)

time = datetime.now()
result = (arrListA == arrListB)
timeList = datetime.now() - time 
print("List Script Time: ", end = " ")
print(time)

if (timeNumpy > timeList):
    print("NumPy is Winning!")
elif (timeNumpy < timeList):
    print("Lists are Winning! Wooow")
else:
    print("Draw..")

print()
print()

#        
# Comparing time on 
# 1000x1000 Elements
#

arrNumpyA  = np.random.randint(10, size = [1000,1000])
arrNumpyB = np.random.randint(10, size = [1000,1000])

arrListA = arrNumpyA.tolist()
arrListB = arrNumpyB.tolist()

print("1000x1000 Serious Competition is Beginning... It is not a Joke at all!")

time = datetime.now()
result = np.array_equal(arrNumpyA, arrNumpyB)
timeNumpy = datetime.now() - time 
print("NumPy Script Time: ", end = " ")
print(time)

time = datetime.now()
result = (arrListA == arrListB)
timeList = datetime.now() - time 
print("List Script Time: ", end = " ")
print(time)

if (timeNumpy > timeList):
    print("NumPy is Winning!")
elif (timeNumpy < timeList):
    print("Lists are Winning! Wooow")
else:
    print("Draw..")

print()
print()

#        
# Comparing time on 
# 1000x1000 Elements
#

arrNumpyA  = np.random.randint(10, size = [10000,10000])
arrNumpyB = np.random.randint(10, size = [10000,10000])

arrListA = arrNumpyA.tolist()
arrListB = arrNumpyB.tolist()

print("10000x10000 Final. Really Crazy Cometition.. for your device!")

time = datetime.now()
result = np.array_equal(arrNumpyA, arrNumpyB)
timeNumpy = datetime.now() - time 
print("NumPy Script Time: ", end = " ")
print(time)

time = datetime.now()
result = (arrListA == arrListB)
timeList = datetime.now() - time 
print("List Script Time: ", end = " ")
print(time)

if (timeNumpy > timeList):
    print("NumPy is Winning!")
elif (timeNumpy < timeList):
    print("Lists are Winning! Wooow")
else:
    print("Draw..")

print()
print()
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

#### Номер 6
```
import pylab
import numpy as np
from matplotlib import mlab

# Здесь функция, вычисляющая игрек
def func (t):
  return (np.e**(-1 * t) * np.cos(2 * np.pi * t))

tmin = -10
tmax = 10
step = 0.01

# !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы. Создание массива с иксами.
tlist = mlab.frange(tmin, tmax, step)

# Вычислим значение функции в заданных точках
ylist = [func (x) for x in tlist]

# !!! Нарисуем одномерный график
pylab.plot(tlist, ylist)

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

#### Номер 6
```
import math
import pylab
import numpy as np
from matplotlib import mlab

def func (t):
    return (np.e**(-1 * t) * np.cos(2 * np.pi * t))

tmin = -10
tmax = 10
step = 0.01

# !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
tlist = mlab.frange(tmin, tmax, step)

# Вычислим значение функции в заданных точках
ylist = [func (x) for x in tlist]

# !!! Нарисуем одномерный график
pylab.plot(tlist, ylist, "--b")

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

#### Номер 6
```
import pylab
import numpy as np
from matplotlib import mlab

def function1 (t):
    return (np.e**(-1 * t) * np.cos(2 * np.pi * t))

def function2 (t):
    return (-1 * np.e**(-1 * t) * np.cos(2 * np.pi * t))

def function3 (t):
    return (2 * np.e**(-1 * t) * np.cos(2 * np.pi * t))

tmin = -10
tmax = 10
step = 0.01

tlist = mlab.frange(tmin, tmax, step)
ylist_1 = [function1(t) for t in tlist]
ylist_2 = [function2(t) for t in tlist]
ylist_3 = [function3(t) for t in tlist]

pylab.plot(tlist, ylist_1, "-.b", label="     f(x)")
pylab.plot(tlist, ylist_2, "--r", label="-1 * f(x)")
pylab.plot(tlist, ylist_3, "-.g", label=" 2 * f(x)")

pylab.grid()
pylab.legend(loc='upper left') 
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

#### Номер 6
```
import pylab
import numpy
import matplotlib.pyplot as plt

def makeData ():
    x = numpy.arange(-3, 3, 0.1)
    y = numpy.arange(-3, 3, 0.1)
    
    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid = xgrid * xgrid + ygrid * ygrid - ygrid
    
    return xgrid, ygrid, zgrid

    x, y, z = makeData()

    fig = pylab.figure()

    cs = plt.contourf(x, y, z, 100)

    plt.colorbar(cs)
    plt.show()
```



```
15.Выполнить обработку элементов прямоугольной матрицы ,
имеющей строк и столбцов. Определить, сколько нулевых
элементов содержится в каждом столбце и в каждой строке матрицы.
Результат оформить в виде матрицы из строк и
столбцов.
```

```
import numpy as np
import random

n = int(input("Enter n >> "))
m = int(input("Enter m >> "))
a = np.zeros((n,m))

b = []

for i in range(n):
  q = 0
  for j in range(m):
    a[i][j] = np.floor(random.random() * 200 - 100)
    if (a[i][j] == 0):
      q = q + 1
    b.append(q)

for i in range(n):
  for j in range(m):
    print(a[i][j], end=" | ")
  print()

print("------")

for i in range(n):
  print(b[i], end=" ")

print()

print("------")

c=[]
for j in range(m):
  q = 0
  for i in range(n):
    if (a[i][j] == 0):
      q = q + 1
  c.append(q)

for i in range(m):
  print(c[i])

```





## Часть 4 | Pandas

```
import pandas as pd

df = pd.read_csv("titanic.csv")
print(df)

# Чему равно число погибших?
print("Amount of survived ", len(df.loc[df["Survived"]==0]))

# Какой процент спасшиеся женщины и дети составляют от общего количества женщин и детей?
sp = len(df.loc[(df["Sex"] == "female") & (df["Age"] >= 18)])
g = len(df.loc[df["Age"] < 18])
w = sp + g
vsp = len(df.loc[(df["Sex"] == "female") & (df["Age"] >= 18) & (df["Survived"]==1)])
vg = len(df.loc[(df["Age"] < 18) & (df["Survived"] == 1)])
h = vsp + vg
f = (h * 100) / w
print("% Women and Children of All the Women and Children ", round(f,2))

# А спасшиеся мужчины от общего количества мужчин?
mp = len(df.loc[(df["Sex"] == "male")])
mv = len(df.loc[(df["Sex"] == "male") & (df["Survived"] == 1)])
km = (mv * 100) / mp
print("% Men Survived of All the Men", round(km,2))

# Какую долю пассажиры первого класса составляли среди всех пассажиров?
klsc = len(df.loc[(df["Pclass"] == 1)])
kls = len(df.loc[(df["Pclass"])])
klw = (klsc * 100) / kls
print("% First Class Passengers of All", round(klw,2))

# Какой процент детей от общего числа пассажиров?
ch = len(df.loc[(df["Age"] < 18)])
all = len(df.loc[(df["PassengerId"])])
chp = (ch * 100) / all
print("% Children of All ", round(chp,2), "%")
```


## Финал

```
import pandas as pd
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

print ('Quantity of raws ',df['PassengerId'].count())
print ('Median ',df['Age'].median())
print ('Moda ',df['Age'].mode())
print ('Average Value ',df['Age'].mean())
print ('Min ',df['Age'].min())
print ('Max ',df['Age'].max())

df['Difference'] = df['Age'].max() - df['Age'].min()
print(df)

b1=df[(df['Age'] <= 20) & (df['Age'] > 30)]
print (b1)

b2=df[(df['Age'] <= 30) & (df['Age'] > 40)]
print (b2)

b3=df[(df['Age'] <= 41) & (df['Age'] > 50)]
print (b3)

# PLOTS

# Plot data
labels = ["b1", "b2", "b3"]
data = [b1['Age'].count(),b2['Age'].count(),b3['Age'].count()]

# Drawing plots
fig = plt.figure()
plt.pie (data,labels=labels)
fig.savefig('circleDiagramm.png')

# Drawing Histogrammas
fig1 = plt.figure()
b1['Age'].hist()
fig1.savefig('figure1.png')

fig2 = plt.figure()
b2['Age'].hist()
fig2.savefig('figure2.png')

fig3 = plt.figure()
b3['Age'].hist()
fig3.savefig('figure3.png')

# Creating seperate CSVs
r1 = b1.groupby(['Age']).mean()
r1.to_csv('r1.csv')
r1.sort_values(by=['Age', 'Sex'])
print(r1)

r2 = b2.groupby(['Age']).mean()
r2.to_csv('r2.csv')
r2.sort_values(by=['Age', 'Name'])
print(r2)

r3=b3.groupby(['Age']).mean()
r3.to_csv('r3.csv')
r3.sort_values(by=['Sex', 'Name'])
print(r3)
```
