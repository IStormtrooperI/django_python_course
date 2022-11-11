print('''
    Агенство недвижимости
    Арендуемые квартиры''')
currentCommand = ''
isExitToMainMenu = False
#id,адрес,кол-во комнат, площадь, цена, наличие лифта, имена жильцов
table = [[1, "Пушкина д.25 кв.1", 100, 1000.26, 50000000.43, "да", ["Альфавит Петр Николаевич", "Казах Владимир Петрович"]],
         [2, "Пушкина д.25 кв.2", 50, 1000.23, 503204.31, "да", ["Вафель Александр Петрович"]],
         [3, "Пушкина д.26 кв.1", 4, 4123.23, 21453.31, "нет", ["Петров Петр Петрович"]],
         [4, "Пушкина д.26 кв.2", 8, 523.23, 78652.31, "нет", ["Александров Алексей Александрович"]],
         [5, "Пушкина д.26 кв.3", 2, 4123.23, 6432.31, "нет", ["Алексеев Петр Николаевич"]]]
while True:
    print('''
    Меню
    Введите одну из команд:
    1 - Добавить объект
    2 - Удалить объект
    3 - Поиск объекта по номеру
    4 - Список объектов
    5 - Фильтр по атрибуту объекта
    6 - Средний показатель по атрибуту объекта
    exit - Выйти из программы
    ''')
    currentCommand = input()
    if currentCommand == "1":
        objectIndex = table[-1][0]+1
        table.append([objectIndex, '', 0, 0.00, 0.00, '', []])
        print('''
Добавление объекта, введите по очереди: адрес, количество комнат, площадь, цену, наличие лифта и ФИО текущих жильцов,
либо введите в любой момент команду: {exit} для выхода в главное меню и удаления незаполненного объекта
        ''')
        while True:
            if isExitToMainMenu == True:
                isExitToMainMenu = False
                break
            elif table[-1][1] == '':
                print("Введите адрес квартиры")
                currentCommand = input()
                if currentCommand.lower() == "exit":
                    table.pop(-1)
                    break
                table[-1][1] = currentCommand
            elif table[-1][2] == 0:
                print("Введите количество комнат")
                currentCommand = input()
                if currentCommand.lower() == "exit":
                    table.pop(-1)
                    break
                try:
                    table[-1][2] = int(currentCommand)
                except:
                    print("Ошибка! Было введено не цифровое значение")
                    continue
            elif table[-1][3] == 0.00:
                print("Введите площадь квартиры")
                currentCommand = input()
                if currentCommand.lower() == "exit":
                    table.pop(-1)
                    break
                try:
                    table[-1][3] = float(currentCommand)
                except:
                    print("Ошибка! Было введено не цифровое значение")
                    continue
            elif table[-1][4] == 0.00:
                print("Введите цену квартиры")
                currentCommand = input()
                if currentCommand.lower() == "exit":
                    table.pop(-1)
                    break
                try:
                    table[-1][4] = float(currentCommand)
                except:
                    print("Ошибка! Было введено не цифровое значение")
                    continue
            elif table[-1][5] == '':
                print("Введите наличие/отсутствие лифта {да/нет}")
                currentCommand = input()
                if currentCommand.lower() == "exit":
                    table.pop(-1)
                    break
                elif currentCommand.lower() == "да" or currentCommand.lower() == "нет":
                    table[-1][5] = currentCommand.lower()
                else:
                    print("Ошибка! Было введено некорректное значение")
                    continue
            elif len(table[-1][6]) == 0:
                print('''
Введите список текущих жильцов по очереди(ФИО полностью), 
если вы ввели хотя бы одного жильца и хотите закончить ввод жильцов, 
введите команду: thatsall
                ''')
                while True:
                    currentCommand = input()
                    if currentCommand.lower() == "exit":
                        table.pop(-1)
                        isExitToMainMenu = True
                        break
                    elif currentCommand.lower() == "thatsall" and len(table[-1][6]) > 0:
                        break
                    elif currentCommand.lower() == "thatsall" and len(table[-1][6]) == 0:
                        print("Ошибка! Для завершения ввода жильцов необходимо ввести хотя бы одного жильца")
                    try:
                        partsName = currentCommand.split()
                        if len(partsName) == 3:
                            table[-1][6].append(currentCommand)
                            continue
                    except:
                        print("Ошибка! Было введено некорректное значение")
                        continue
            else:
                print("Был добавлен новый объект:")
                for element in table[-1]:
                    print(element, end=' | ')
                break
    elif currentCommand == "2":
        while True:
            print("Введите номер объекта для удаления, либо {exit} для выхода в главное меню")
            currentCommand = input()
            if currentCommand == "exit":
                print("Выход в главное меню")
                break
            try:
                print("Объект для удаления:")
                for index,str in enumerate(table):
                    if str[0] == int(currentCommand):
                        for element in str:
                            print(element, end=' | ')
                        table.pop(index)
                        print("\n был удален.")
            except:
                print("не был найден.")
    elif currentCommand == "3":
        while True:
            print("Введите номер объекта для поиска, либо {exit} для выхода в главное меню")
            currentCommand = input()
            if currentCommand == "exit":
                print("Выход в главное меню")
                break
            try:
                print("Объект для поиска:")
                for index,str in enumerate(table):
                    if str[0] == int(currentCommand):
                        for element in str:
                            print(element, end=' | ')
                        print("\n был найден.")
            except:
                print("не был найден.")
    elif currentCommand == "4":
        print("номер", "адрес", "количество комнат", "площадь", "цену", "наличие лифта", "ФИО текущих жильцов", sep=" | ")
        for str in table:
            for element in str:
                print(element, end=" | ")
            print()
    elif currentCommand == "5":
        print('''
Фильтр по наличию лифта в здании:
да - лифт есть в здании,
нет - лифта нет в здании

Фильтр по количеству комнат в квартире:
Введите до какого количества комнат должна быть квартира

exit - выйти в главное меню
        ''')
        currentCommand = input()
        if currentCommand == "exit":
            print("Выход в главное меню")
            break
        elif currentCommand.lower() == "да":
            for str in table:
                if str[5] == "да":
                    for element in str:
                        print(element, end=" | ")
                print()
        elif currentCommand.lower() == "нет":
            for str in table:
                if str[5] == "нет":
                    for element in str:
                        print(element, end=" | ")
                print()
        else:
            try:
                currentLessRooms = int(currentCommand)
                for str in table:
                    if str[2] <= currentLessRooms:
                        for element in str:
                            print(element, end=" | ")
                        print("\n")
            except:
                print("Ошибка! Было введено некорректное значение")
    elif currentCommand == "6":
        while True:
            print('''
Выберите атрибут, по которому необходимо посчитать средний показатель:
    количество комнат, площадь, цена
    для выхода в главное меню введите {exit}
            ''')
            currentCommand = input()
            if currentCommand == "exit":
                print("Выход в главное меню")
                break
            sumElements = 0
            if currentCommand.lower() == "количество комнат":
                for strElement in table:
                    sumElements += strElement[2]
                print("Среднее количество комнат: ", round(sumElements/len(table), 2))
            elif currentCommand.lower() == "площадь":
                for strElement in table:
                    sumElements += strElement[3]
                print("Средняя площадь: ", round(sumElements/len(table), 2))
            elif currentCommand.lower() == "цена":
                for strElement in table:
                    sumElements += strElement[4]
                print("Средняя цена: ", round(sumElements/len(table), 2))
    elif currentCommand == "exit":
        print("Выход из программы")
        break
    else:
        print("Ошибка! Некорректная команда.")
        continue