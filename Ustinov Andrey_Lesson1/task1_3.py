# 3. Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».


percent = int(input('Введите число от 1 до 20:'))

if percent == 1:
    print(f'{percent} процент')
elif (percent >= 2) and (percent < 5):
    print(f'{percent} процента')
elif (percent > 4) and (percent < 21):
    print(f'{percent} процентов')
else:
    print('Вы ввели число не соответсвующее условию')

# Вывести все склонения для проверки.

for i in range(1, 21):
    if i == 1:
        print(f'{i} процент')
    elif (i >= 2) and (i < 5):
        print(f'{i} процента')
    else:
        print(f'{i} процентов')