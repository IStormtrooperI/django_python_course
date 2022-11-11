def provRubl(n):
    try:
        n = int(n)
        prov = n % 10
        prov2 = n % 100
        if n < 1:
            print('Введено некорректное значение, введите натуральное число больше 0')
        elif 9 >= prov >= 5 or prov == 0 or 19 >= prov2 >= 11:
          print(n, ' рублей')
        elif 4 >= prov >= 2:
          print(n, 'рубля')
        elif prov == 1:
          print(n, 'рубль')
    except:
        print('Введено некорректное значение, введите натуральное число больше 0')
print('Подставление рубля к числу, введите число:')
provRubl(input())



