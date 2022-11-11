print("Аптечный калькулятор")

try:
    count = int(input("Сколько витаминок хотите купить? "))
    if count < 1:
        raise Exception("Ошибка! было введено число меньше 1.")

    try:
        cost = float(input("По какой цене? "))
        if cost < 1:
            raise Exception("Ошибка! было введено число меньше 1.")

        try:
            karta = input("Есть ли у Вас социальная карта? ")
            if (karta != "yes" or karta != "no" or karta != "Да" or karta != "Нет" or karta != "нет" or karta != "да") == False:
                raise Exception("Ошибка! было введено некорректное значение. Введите Да или Нет")

            print("# Чек")

            if count < 5:
                print("# Вам положена обычная цена!")
            elif 10 > count >= 5:
                print("# Вам положена скидка 10%!")
                skidka = 10
            elif count > 10:
                free = int(count // 10)
                print("# Каждая 10-я аскорбинка бесплатно! ")

            print("# Соц. карта: ", karta)

            sum = count * cost

            print("# Сумма покупки ", round(sum,2), " р.")

            if 'skidka' in locals() and (karta == "Да" or karta == "да" or karta == "yes"):
                sum_skidka = sum * ((skidka + 10) / 100)
                print("# Скидка", round(sum_skidka, 2), " р.")
            elif 'free' in locals() and (karta == "Да" or karta == "да" or karta == "yes"):
                sum_skidka = sum * (10 / 100) + (free * cost)
                print("# Скидка", round(sum_skidka, 2), " р.")
            elif 'free' in locals() and (karta == "Нет" or karta == "нет" or karta == "no"):
                sum_skidka = free * cost
                print("# Скидка", round(sum_skidka, 2), " р.")
            elif 'skidka' in locals() and (karta == "Нет" or karta == "нет" or karta == "no"):
                sum_skidka = sum * ((skidka) / 100)
                print("# Скидка", round(sum_skidka, 2), " р.")

            print("# Итого ", round(sum - sum_skidka, 2), "р.")


        except:
            print("Ошибка!")
    except:
        print("Ошибка! было введено не числовое значение.")
except:
    print("Ошибка! было введено не числовое значение.")

print("Завершение программы")