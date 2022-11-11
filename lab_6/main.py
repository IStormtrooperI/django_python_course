import csv
import numpy as np
import matplotlib.pylab as pylab
from scipy.interpolate import make_interp_spline, BSpline

playersAndMatches = {"players": dict(), "matches": dict()}
countBirthdayInMonth = dict()
countsPositions = {"positions": {0: "G", 1: "D", 2: "F"}, "counts": {0: 0, 1: 0, 2: 0}}
playersOfG = {"year": dict(), "height": dict()}
playersOfF = {"year": dict(), "height": dict()}
playersOfD = {"year": dict(), "height": dict()}
with open("hockey_players.csv", mode='r', encoding='ANSI') as csvFile:
    file_reader = csv.DictReader(csvFile, fieldnames=None, dialect="excel")
    # print(file_reader)
    for index, row in enumerate(file_reader):
        row["name"].replace("\xa0", " ")
        monthOfBirth = int(row["birth"][5:7])

        if monthOfBirth in countBirthdayInMonth.keys():
            countBirthdayInMonth[monthOfBirth] += 1
        else:
            countBirthdayInMonth[monthOfBirth] = 1

        for position in countsPositions["positions"].items():
            if row["position"] == position[1]:
                countsPositions["counts"][position[0]] += 1

        if row["name"] not in playersAndMatches["players"].values():
            playersAndMatches["players"][len(playersAndMatches["players"])] = row["name"]
            playersAndMatches["matches"][len(playersAndMatches["players"])] = 1
        else:
            for player in playersAndMatches["players"].items():
                if player[1] == row["name"]:
                    playersAndMatches["matches"][player[0]] += 1

        if row["position"] == "G":
                playersOfG["year"][len(playersOfG["year"])] = int(row["year"])
                playersOfG["height"][len(playersOfG["height"])] = float(row["height"])
                continue

        if row["position"] == "F":
                playersOfF["year"][len(playersOfF["year"])] = int(row["year"])
                playersOfF["height"][len(playersOfF["height"])] = float(row["height"])
                continue

        if row["position"] == "D":
                playersOfD["year"][len(playersOfD["year"])] = int(row["year"])
                playersOfD["height"][len(playersOfD["height"])] = float(row["height"])
                continue

playersAndCountsPlaying = {"countPlayers": 0, "countPlaying": dict()}

while len(playersAndCountsPlaying["countPlaying"]) != 16:
    playersAndCountsPlaying["countPlaying"][len(playersAndCountsPlaying["countPlaying"]) + 1] = 0
for matches in playersAndMatches["matches"].items():
    playersAndCountsPlaying["countPlayers"] = matches[0]
    playersAndCountsPlaying["countPlaying"][matches[1]] += 1
proportionOfPlayers = dict()
for count in playersAndCountsPlaying["countPlaying"].values():
    proportionOfPlayers[len(proportionOfPlayers) + 1] = count / playersAndCountsPlaying["countPlayers"]

heightOfPlayersInYearG = {"year": dict(), "height": dict()}
heightOfPlayersInYearF = {"year": dict(), "height": dict()}
heightOfPlayersInYearD = {"year": dict(), "height": dict()}
year = 1
count = 0

for currentYear in playersOfG["year"].items():
    if currentYear[1] == year:
        heightOfPlayersInYearG["height"][len(heightOfPlayersInYearG["height"]) - 1] += playersOfG["height"][currentYear[0]]
        count += 1
    else:
        if len(heightOfPlayersInYearG["height"]) > 0:
            heightOfPlayersInYearG["height"][len(heightOfPlayersInYearG["height"]) - 1] /= count
            count = 0
        heightOfPlayersInYearG["year"][len(heightOfPlayersInYearG["year"])] = currentYear[1]
        heightOfPlayersInYearG["height"][len(heightOfPlayersInYearG["height"])] = playersOfG["height"][currentYear[0]]
        count += 1
    if currentYear[0] == len(playersOfG["year"]) - 1:
        heightOfPlayersInYearG["height"][len(heightOfPlayersInYearG["height"]) - 1] /= count
        count = 0
    year = currentYear[1]
count = 0

for currentYear in playersOfF["year"].items():
    if currentYear[1] == year:
        heightOfPlayersInYearF["height"][len(heightOfPlayersInYearF["height"]) - 1] += playersOfF["height"][currentYear[0]]
        count += 1
    else:
        if len(heightOfPlayersInYearF["height"]) > 0:
            heightOfPlayersInYearF["height"][len(heightOfPlayersInYearF["height"]) - 1] /= count
            count = 0
        heightOfPlayersInYearF["year"][len(heightOfPlayersInYearF["year"])] = currentYear[1]
        heightOfPlayersInYearF["height"][len(heightOfPlayersInYearF["height"])] = playersOfF["height"][currentYear[0]]
        count += 1
    if currentYear[0] == len(playersOfF["year"]) - 1:
        heightOfPlayersInYearF["height"][len(heightOfPlayersInYearF["height"]) - 1] /= count
        count = 0
    year = currentYear[1]
count = 0

for currentYear in playersOfD["year"].items():
    if currentYear[1] == year:
        heightOfPlayersInYearD["height"][len(heightOfPlayersInYearD["height"]) - 1] += playersOfD["height"][currentYear[0]]
        count += 1
    else:
        if len(heightOfPlayersInYearD["height"]) > 0:
            heightOfPlayersInYearD["height"][len(heightOfPlayersInYearD["height"]) - 1] /= count
            count = 0
        heightOfPlayersInYearD["year"][len(heightOfPlayersInYearD["year"])] = currentYear[1]
        heightOfPlayersInYearD["height"][len(heightOfPlayersInYearD["height"])] = playersOfD["height"][currentYear[0]]
        count += 1
    if currentYear[0] == len(playersOfD["year"]) - 1:
        heightOfPlayersInYearD["height"][len(heightOfPlayersInYearD["height"]) - 1] /= count
        count = 0
    year = currentYear[1]

#print(playersAndCountsPlaying)
#print(list(proportionOfPlayers.values()))

pylab.figure(figsize=(14, 12))

pylab.subplot(2, 2, 1)

#pylab.subplots_adjust(wspace=100, hspace=100)

y_pos = np.arange(len(proportionOfPlayers.keys()))
pylab.bar(y_pos, list(proportionOfPlayers.values()), color='red', edgecolor='black')
pylab.xticks(y_pos, list(proportionOfPlayers.keys()))
pylab.title("Распределение хoккеистов по количеству участий в ЧМ")
pylab.xlabel("Количество ЧМ")
pylab.ylabel("Доля")

pylab.subplot(2, 2, 2)

#print(heightOfPlayersInYearG)
#print(heightOfPlayersInYearF)
#print(heightOfPlayersInYearD)

xG = list(heightOfPlayersInYearG["year"].values())
yG = list(heightOfPlayersInYearG["height"].values())
polyfitG = np.polyfit(xG, yG, 1)
poly1dG = np.poly1d(polyfitG)
xF = list(heightOfPlayersInYearF["year"].values())
yF = list(heightOfPlayersInYearF["height"].values())
polyfitF = np.polyfit(xF, yF, 1)
poly1dF = np.poly1d(polyfitF)

xD = list(heightOfPlayersInYearD["year"].values())
yD = list(heightOfPlayersInYearD["height"].values())
polyfitD = np.polyfit(xD, yD, 1)
poly1dD = np.poly1d(polyfitD)

pylab.plot(xG, poly1dG(xG), linestyle="--", color="#1f77b4", label="Вратарь")
pylab.plot(xF, poly1dF(xF), linestyle="--", color="#2ca02c", label="Нападающий")
pylab.plot(xD, poly1dD(xD), linestyle="--", color="#ff7f0e", label="Защитник")
pylab.title("Тренды изменения роста игрока для каждой позиции")
pylab.ylabel("Рост (см.)")
pylab.xlabel("Год ЧМ")
pylab.legend()#loc="lower right"

#print(countBirthdayInMonth)
countBirthdayInMonth = dict(sorted(countBirthdayInMonth.items(), key=lambda x: x[0]))
headMonths = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]

pylab.subplot(2, 2, 3)

y_pos = np.arange(len(countBirthdayInMonth.keys()))
pylab.bar(y_pos, list(countBirthdayInMonth.values()))
pylab.xticks(y_pos, headMonths)
pylab.title("Распределение хоккеистов по месяцам рождения")
pylab.xlabel("")
pylab.ylabel("Чел.")

#print(countsPositions)
headPositions = ["Вратарь", "Защитник", "Нападающий"]

pylab.subplot(2, 2, 4)

pylab.pie(list(countsPositions["counts"].values()), labels=headPositions, colors=['#2ca02c', '#ff7f0e', '#1f77b4'], autopct='%1.1f%%', textprops={"fontsize": 14})
pylab.title("Распределение позиций между хоккеистами")

pylab.show()