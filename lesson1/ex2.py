sec = int(input("Введите время в секундах: "));
h = int(sec / 3600);
sec = sec - (h * 3600);
min = int(sec / 60);
sec = sec - (min * 60);
#print(f"{h} : {min} : {sec} ");
#print(h);
#print(min);
#print(sec);
print('{:02}'.format(h), ":", '{:02}'.format(min), ":", '{:02}'.format(sec))