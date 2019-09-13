'''
Дано число n. Напечатать те натуральные числа, квадрат которых не превышает n.

n = int(input("Enter n: "))
i = 1
while (i * i <= n):
  print(i)
  i += 1


Дан целочисленный массив размера N. Вывести вначале все содержащиеся в данном
массиве четные числа в порядке возрастания их индексов, а затем — все нечетные
числа в порядке убывания их индексов. 

n = int(input("Enter n: "))
numbers = []
for i in range(n):
  num = int(input("numbers[%d]:" % i))
  numbers.append(num)
  i += 1

i = 0
while i < len(numbers):
  if (numbers[i] % 2 == 0):
    print(numbers[i])
  i += 1

print("---")

i = len(numbers) - 1
while i >= 0:
  if (numbers[i] % 2 == 1):
    print(numbers[i])
  i -= 1


Дан массив размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти сумму всех
элементов массива, кроме элементов с номерами от K до L включительно.  

n = int(input("Enter n: "))
numbers = []
for i in range(n):
  num = int(input("numbers[%d]:" % i))
  numbers.append(num)
  i += 1
print("---")

k = int(input("Enter k:"))
l = int(input("Enter l:"))

i = 0
sum = 0
while i < len(numbers):
  if (i < k or i >= l):
    sum += numbers[i]
  i += 1
print("Sum of array in range is: %d" % sum)


Дана целочисленная матрица размера M × N. Найти количество ее столбцов, все
элементы которых различны. 

'''   
import random

n = int(input("Enter N: "))
m = int(input("Enter M: "))
numbers = []
for i in range(n):
  arr = []
  numbers.append(arr)
  for j in range(m):
    '''num = int(random.random() * 10);'''
    num = int(input())
    numbers[i].append(num)

    j += 1
  i += 1

print("---")

result = 0
for i in range(n):
  foundTheSame = False
  for j in range(m):
    # Сравниваем каждое число в стобце с другим каждым
    # если найдено похожее, то переходим к след. столбцу
    # иначе resul+ продожаем
    for k in range(j, m - 1):
      if (numbers[i][k + 1] == numbers[i][j]):
        foundTheSame = True
        print("___")
        print(i)
        print(k + 1)
        print(j)
        print("--")
        print(numbers[i][k + 1])
        print(numbers[i][j])
        print("Found the same")
        break
      k += 1
    if(foundTheSame):
      break
    j += 1
  if (not foundTheSame):
    result += 1
  i += 1

print("Cols with different values is: %d" % result)
