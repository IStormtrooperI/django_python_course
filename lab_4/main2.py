import pandas
import numpy
#countChildren,gluc,artDav,tolch,insul,indexMas,funcGenD,age,diab
with open('prima-indians-diabetes.csv', newline='') as fileCSV:
    readerCSV = pandas.read_csv(fileCSV)
    copyReaderCSV = readerCSV
    readerCSV = readerCSV.to_dict()
    maxAgeWithD = 0
    countPeopleWithD = 0
    averageAgeWithD = 0
    countPeopleWithoutD = 0
    countPeopleWithoutDAndChildren = 0
    maxGluc = 0
    countPeopleWith80ArtDav = 0
    averagePeopleWith80ArtDav = 0
    copyReaderCSVSort = copyReaderCSV.sort_values(by='age', ascending=True)
    averageInsulin = round(copyReaderCSV['insul'].mean(), 0)
    heads = {0: "countChildren", 1: "gluc", 2: "artDav", 3: "tolch", 4: "insul", 5: "indexMas", 6: "funcGenD", 7: "age", 8: "diab"}
    maxKoefKorrel = 0

    firstP = ''
    secondP = ''
    for keyTable, dictsTable in readerCSV.items():
        count = 0
        while count < 9:
            if heads[count] == keyTable:
                count += 1
                continue
            averageF = copyReaderCSV[keyTable].mean()
            averageS = copyReaderCSV[heads[count]].mean()
            averageFS = (averageF + averageS) / 2
            dispF = 0
            countF = 0
            dispS = 0
            countS = 0
            averageKvF = 0
            averageKvS = 0
            listF = list()
            listS = list()
            for keyF, xF in dictsTable.items():
                dispF = (xF - averageF) * (xF - averageF)
                countF += 1
                listF.append(xF)
            dispF /= countF
            averageKvF = dispF ** 0.5
            for keyS, xS in copyReaderCSV[heads[count]].items():
                dispS = (xS - averageS) * (xS - averageS)
                countS += 1
                listS.append(xS)
            dispS /= countS
            averageKvS = dispS ** 0.5
            koefKorrel = (averageFS - averageF * averageS) / (averageKvF * averageKvS)
            #print(averageFS - averageF * averageS)
            #if isinstance(koefKorrel, complex):
            #    count += 1
            #    continue
            z = numpy.corrcoef(listF, listS)[0, 1]
            #print(z)
            if maxKoefKorrel < z:
                maxKoefKorrel = z
                firstP = keyTable
                secondP = heads[count]
            count += 1
        if keyTable == "diab":
            for key, currentValue in dictsTable.items():
                if currentValue == 1:
                    countPeopleWithD += 1
                    averageAgeWithD += readerCSV['age'][key]
                    if readerCSV['age'][key] > maxAgeWithD:
                        maxAgeWithD = readerCSV['age'][key]
                elif currentValue == 0:
                    countPeopleWithoutD += 1
                    if readerCSV['countChildren'][key] == 0:
                        countPeopleWithoutDAndChildren += 1
        elif keyTable == "age":
            for key, currentValue in dictsTable.items():
                if currentValue >= 50 and readerCSV['gluc'][key] >= maxGluc:
                    maxGluc = readerCSV['gluc'][key]
        elif keyTable == "artDav":
            for key, currentValue in dictsTable.items():
                if currentValue > 80:
                    countPeopleWith80ArtDav += 1
                    averagePeopleWith80ArtDav += readerCSV['age'][key]
    averagePeopleWith80ArtDav /= countPeopleWith80ArtDav
    averageAgeWithD /= countPeopleWithD
    proportionPeopleWithoutChildrenAndD = round(countPeopleWithoutDAndChildren/countPeopleWithoutD,2)

    print("1) максимальный возраст пациентов с диабетом: ", maxAgeWithD)
    print("   средний возраст пациентов с диабетом: ", round(averageAgeWithD,0))
    print("2) параметры: первый - ", firstP, "второй - ", secondP, "значение корреляции: ", maxKoefKorrel)
    print("3) доля бездетных среди пациентов с неустановленным диабетом: ", proportionPeopleWithoutChildrenAndD)
    print("4) максимальная концентрация глюкозы у пациентов старше 50 лет: ", maxGluc)
    print("5) средний возраст пациентов с диастолгическим давлением выше 80: ", round(averagePeopleWith80ArtDav, 0))
    print("6) Список пациентов старше 60 с уровнем инсулина выше среднего, отсортированный по возрастанию столбца Возраст.")
    for keyTable, dictsTable in copyReaderCSVSort.items():
        if keyTable == "age":
            for key, currentValue in dictsTable.items():
                if currentValue > 60 and copyReaderCSVSort['insul'][key] > averageInsulin:
                    print("    ", key, copyReaderCSVSort['countChildren'][key], copyReaderCSVSort['gluc'][key], copyReaderCSVSort['artDav'][key], copyReaderCSVSort['tolch'][key], copyReaderCSVSort['insul'][key], copyReaderCSVSort['indexMas'][key], copyReaderCSVSort['funcGenD'][key], copyReaderCSVSort['age'][key], copyReaderCSVSort['diab'][key], sep=" | ")
    print("7) Список записей с нулевыми значениями хотя бы одного параметра (за исключением первого и последнего столбцов).")
    for keyTable, dictsTable in copyReaderCSV.items():
        if keyTable == "age":
            for key, currentValue in dictsTable.items():
                if currentValue == 0 or copyReaderCSV['gluc'][key] == 0 or copyReaderCSV['artDav'][key] == 0 or copyReaderCSV['tolch'][key] == 0 or copyReaderCSV['insul'][key] == 0 or copyReaderCSV['indexMas'][key] == 0 or copyReaderCSV['funcGenD'][key] == 0:
                    print("    ", key, copyReaderCSV['countChildren'][key], copyReaderCSV['gluc'][key],
                          copyReaderCSV['artDav'][key], copyReaderCSV['tolch'][key], copyReaderCSV['insul'][key],
                          copyReaderCSV['indexMas'][key], copyReaderCSV['funcGenD'][key], copyReaderCSV['age'][key],
                          copyReaderCSV['diab'][key], sep=" | ")

#countChildren,gluc,artDav,tolch,insul,indexMas,funcGenD,age,diab