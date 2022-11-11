import os
import csv
try:
    files = os.listdir("news/")
    datasetCSV = []
    preWord = "0"
    continueNextWord = False
    #print(files)
    #print(datasetCSV)
    for file in files:
        index = ''
        title = ''
        lid = ''
        text = ''
        ner = False
        language = ''
        url = ''
        date = ''
        isRu = False
        isEn = False
        if "news" in file and ".txt" in file:
            #print(file)
            fileOpen = open("news/"+file, 'r', encoding="utf-8")
            lines = fileOpen.readlines()
            index = int(file[4:6])
            for indexLine, line in enumerate(lines):
                if title == '' and line !='\n':
                    line = line.replace("\"", "\'")
                    title = line.strip()
                elif lid == '' and line !='\n':
                    line = line.replace("\"", "\'")
                    lid = line.strip()
                else:
                    line = line.replace("\"", "\'")
                    text += line.strip() + ' '
                if not ner:
                    for indexWord, word in enumerate(line.split()):
                        if indexWord == 0:
                            continue
                        if word[-1] == '.':
                            continueNextWord = True
                            continue
                        if continueNextWord:
                            continueNextWord = False
                            continue
                        if ('A' <= word[0] <= 'Z') or ('А' <= word[0] <= 'Я') or word[0] == 'Ё':
                            ner = True
                            break
                        preWord = word
                if language == "":
                    for indexWord, word in enumerate(line.split()):
                        if (not isEn) and (('A' <= word[0] <= 'Z') or ('a' <= word[0] <= 'z')):
                            isEn = True
                        if (not isRu) and (('А' <= word[0] <= 'Я') or ('а' <= word[0] <= 'я') or word[0] == 'ё' or word[0] == 'Ё'):
                            isRu = True
                        if isEn and isRu:
                            language = 'ru-en'
                            break
                    if language == '' and isEn:
                        language = 'en'
                    elif language == '' and isRu:
                        language = 'ru'
                if 'https' in line:
                    url = line[line.find('https'):]
                    for word in line.split('/'):
                        if len(word) >= 4:
                            try:
                                currentDate = int(word[0:4])
                                try:
                                    if word[4] != '-':
                                        continue
                                except:
                                    currentDate = int(word[0:4])
                                if 2050 >= currentDate >= 1990:
                                    date = currentDate
                            except:
                                continue

        # "Index", "Title", "Lid", "Text", "Ner", "Language", "URL", "Date"
        datasetCSV.append({"Index": index, "Title": title, "Lid": lid, "Text": text, "Ner": ner, "Language": language, "URL": url, "Date": date})
    csv.register_dialect("myDialect", delimiter='|')
    with open("newsCSV.csv", mode='w', encoding='utf-8') as csvFile:
        names = ["Index", "Title", "Lid", "Text", "Ner", "Language", "URL", "Date"]
        file_writer = csv.DictWriter(csvFile, dialect='myDialect', fieldnames=names)
        file_writer.writeheader()
        file_writer.writerows(datasetCSV)
    print("Файл создан")
    #for file in datasetCSV:
        #print(file)
    #print(datasetCSV)
except Exception as ex:
    print(ex)
finally:
    if fileOpen in locals():
        fileOpen.close()
