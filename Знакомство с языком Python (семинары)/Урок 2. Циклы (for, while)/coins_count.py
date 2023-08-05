### Сколько нужно перевернуть монет ###
from random import randint

coins_c = [randint(0, 1) for i in range(20)]
s = len(coins_c)

print('На столе ', s , 'монет.')

### 1-e решение
a = 0
b = 0

for i in coins_c:
    if i == 1:
        a = a + 1
    else:
        b = b + 1

print('Орел = ', a, 'Решка = ', b)
res = 0
if a > b:
    res = b
elif a < b:
    res = a
else:
    res = a or b

print('Нужно перевернуть ', res, 'монет')


### - 2-e решение
###print(coins_c.count(0) if coins_c.count(0) < coins_c.count(1) else coins_c.count(1))




