### Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N ###

n = int(input('Введите число N: '))
two_in_power = 2
power = 1

while two_in_power <= n:
    two_in_power *= 2
    power += 1

print(power - 1, two_in_power // 2)