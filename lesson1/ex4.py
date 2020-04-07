a = int(input("Введите целое положительное число: "));
while a <= 0:
    a = int(input("Вы ввели неподходящее число, попробуйте еще раз: "));
maximum = 0;
while a > 0:
    last = a % 10;
    a = a // 10;
    if last > maximum:
        maximum = last;
print(maximum);
