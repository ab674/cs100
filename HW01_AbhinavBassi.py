# Abhinav Bassi
# CS 100 2014F Section H03
# HW 01: Sept 5, 2014

# 2.18

flowers = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilly of the valley']
print('potato' in flowers)
thorny = [flowers[0], flowers[1], flowers[2]]
print('Thorny:', thorny)
poisonous = [flowers[-1]]
print('Poisonous:', poisonous)
dangerous = thorny + poisonous
print('Dangerous:', dangerous)

# 2.19

import math
x = 0
y = 0
print(math.sqrt((x**2)+(y**2)) <= 10)
x = 10
y = 10
print(math.sqrt((x**2)+(y**2)) <= 10)
x = 6
y = 6
print(math.sqrt((x**2)+(y**2)) <= 10)
x = 7
y = 8
print(math.sqrt((x**2)+(y**2)) <= 10)

# 2.21

s = 'bat'
sreverse = (s[-1] + s[-2] + s[-3])
print(sreverse)

# 2.24

import math
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('List:', lst)
middleindex = math.ceil((len(lst)/2))
print('Middle index:', middleindex)
middlevalue = lst[middleindex-1]
print('Middle value:', middlevalue)
lst.reverse()
print('Reversed:', lst)
lst.append(9)
lst.remove(9)
print('Modified:', lst)
