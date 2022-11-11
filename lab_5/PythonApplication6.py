import copy
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import numpy

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Midori/0.4'}

#urlLocal = "urlLocal.html"
#html = BeautifulSoup(Path(urlLocal).read_text(encoding="utf-8"), 'html.parser')

url = "https://soccer365.ru/competitions/13/"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

dataPlayers = {"team": dict(), "player": dict(), "role": dict(), "goals": dict(),
               "penalties": dict(), "passes": dict(), "matches": dict(),
               "isPenalty": dict(), "fairPlay": dict(), "yellowCard": dict(),
               "twoYellowCard": dict(), "redCard": dict()}

mainTable = html.find("table", attrs={"class": "stngs"})

tables = html.find_all("table", attrs={"class": "comp_table_v2"})

trs0 = tables[0].find("tbody").find_all("tr")
# print(trs)

for tr in trs0:
    srcTeam = tr.find("img")["src"]
    team = mainTable.find("img", attrs={"src": srcTeam}).next.a.text
    player = tr.td.div.span.a.text
    role = "бомбардир"

    isPlayerInAssists = tables[1].find("a", string=player)

    if isPlayerInAssists is not None:
        role += ", ассистент"
        passes = int(isPlayerInAssists.parent.parent.parent.parent.find("td", attrs={"class": "bkcenter"}).b.text)
        isPlayerInAssists.parent.parent.parent.parent.decompose()
    else:
        passes = 0

    tds = tr.find_all("td", attrs={"class": "bkcenter"})
    goals = int(tds[0].b.text)
    textPenalties = tds[1].text
    matches = int(tds[2].text)

    if not textPenalties.isspace():
        penalties = int(textPenalties)
    else:
        penalties = 0

    isPlayerInPenalties = tables[2].find("a", string=player)

    if isPlayerInPenalties is not None:
        tdsPenalties = isPlayerInPenalties.parent.parent.parent.parent.find_all("td", attrs={"class": "bkcenter"})
        isPenalty = True

        if not tdsPenalties[0].b.text.isspace():
            fairPlay = int(tdsPenalties[0].b.text)
        else:
            fairPlay = 0

        if not tdsPenalties[1].text.isspace():
            yellowCard = int(tdsPenalties[1].text)
        else:
            yellowCard = 0

        if not tdsPenalties[2].text.isspace():
            twoYellowCard = int(tdsPenalties[2].text)
        else:
            twoYellowCard = 0

        if not tdsPenalties[3].text.isspace():
            redCard = int(tdsPenalties[3].text)
        else:
            redCard = 0
        isPlayerInPenalties.parent.parent.parent.parent.decompose()
    else:
        isPenalty = False
        fairPlay = 0
        yellowCard = 0
        twoYellowCard = 0
        redCard = 0
    dataPlayers["team"][len(dataPlayers["team"])] = team
    dataPlayers["player"][len(dataPlayers["player"])] = player
    dataPlayers["role"][len(dataPlayers["role"])] = role
    dataPlayers["goals"][len(dataPlayers["goals"])] = goals
    dataPlayers["penalties"][len(dataPlayers["penalties"])] = penalties
    dataPlayers["passes"][len(dataPlayers["passes"])] = passes
    dataPlayers["matches"][len(dataPlayers["matches"])] = matches
    dataPlayers["isPenalty"][len(dataPlayers["isPenalty"])] = isPenalty
    dataPlayers["fairPlay"][len(dataPlayers["fairPlay"])] = fairPlay
    dataPlayers["yellowCard"][len(dataPlayers["yellowCard"])] = yellowCard
    dataPlayers["twoYellowCard"][len(dataPlayers["twoYellowCard"])] = twoYellowCard
    dataPlayers["redCard"][len(dataPlayers["redCard"])] = redCard

trs1 = tables[1].find("tbody").find_all("tr")
for tr in trs1:
    srcTeam = tr.find("img")["src"]
    team = mainTable.find("img", attrs={"src": srcTeam}).next.a.text
    player = tr.td.div.span.a.text
    role = "ассистент"
    tdsAssists = tr.find_all("td", attrs={"class": "bkcenter"})
    passes = int(tdsAssists[0].b.text)
    matches = int(tdsAssists[1].text)

    isPlayerInPenalties = tables[2].find("a", string=player)

    if isPlayerInPenalties is not None:
        tdsPenalties = isPlayerInPenalties.parent.parent.parent.parent.find_all("td", attrs={"class": "bkcenter"})
        isPenalty = True

        if not tdsPenalties[0].b.text.isspace():
            fairPlay = int(tdsPenalties[0].b.text)
        else:
            fairPlay = 0

        if not tdsPenalties[1].text.isspace():
            yellowCard = int(tdsPenalties[1].text)
        else:
            yellowCard = 0

        if not tdsPenalties[2].text.isspace():
            twoYellowCard = int(tdsPenalties[2].text)
        else:
            twoYellowCard = 0

        if not tdsPenalties[3].text.isspace():
            redCard = int(tdsPenalties[3].text)
        else:
            redCard = 0
        isPlayerInPenalties.parent.parent.parent.parent.decompose()
    else:
        isPenalty = False
        fairPlay = 0
        yellowCard = 0
        twoYellowCard = 0
        redCard = 0
    dataPlayers["team"][len(dataPlayers["team"])] = team
    dataPlayers["player"][len(dataPlayers["player"])] = player
    dataPlayers["role"][len(dataPlayers["role"])] = role
    dataPlayers["goals"][len(dataPlayers["goals"])] = 0
    dataPlayers["penalties"][len(dataPlayers["penalties"])] = 0
    dataPlayers["passes"][len(dataPlayers["passes"])] = passes
    dataPlayers["matches"][len(dataPlayers["matches"])] = matches
    dataPlayers["isPenalty"][len(dataPlayers["isPenalty"])] = isPenalty
    dataPlayers["fairPlay"][len(dataPlayers["fairPlay"])] = fairPlay
    dataPlayers["yellowCard"][len(dataPlayers["yellowCard"])] = yellowCard
    dataPlayers["twoYellowCard"][len(dataPlayers["twoYellowCard"])] = twoYellowCard
    dataPlayers["redCard"][len(dataPlayers["redCard"])] = redCard

trs2 = tables[2].find("tbody").find_all("tr")
for tr in trs2:
    srcTeam = tr.find("img")["src"]
    team = mainTable.find("img", attrs={"src": srcTeam}).next.a.text
    player = tr.td.div.span.a.text
    role = "не определено"

    tdsPenalties = tr.find_all("td", attrs={"class": "bkcenter"})
    matches = int(tdsPenalties[4].text)
    isPenalty = True

    if not tdsPenalties[0].b.text.isspace():
        fairPlay = int(tdsPenalties[0].b.text)
    else:
        fairPlay = 0

    if not tdsPenalties[1].text.isspace():
        yellowCard = int(tdsPenalties[1].text)
    else:
        yellowCard = 0

    if not tdsPenalties[2].text.isspace():
        twoYellowCard = int(tdsPenalties[2].text)
    else:
        twoYellowCard = 0

    if not tdsPenalties[3].text.isspace():
        redCard = int(tdsPenalties[3].text)
    else:
        redCard = 0
    dataPlayers["team"][len(dataPlayers["team"])] = team
    dataPlayers["player"][len(dataPlayers["player"])] = player
    dataPlayers["role"][len(dataPlayers["role"])] = role
    dataPlayers["goals"][len(dataPlayers["goals"])] = 0
    dataPlayers["penalties"][len(dataPlayers["penalties"])] = 0
    dataPlayers["passes"][len(dataPlayers["passes"])] = 0
    dataPlayers["matches"][len(dataPlayers["matches"])] = matches
    dataPlayers["isPenalty"][len(dataPlayers["isPenalty"])] = isPenalty
    dataPlayers["fairPlay"][len(dataPlayers["fairPlay"])] = fairPlay
    dataPlayers["yellowCard"][len(dataPlayers["yellowCard"])] = yellowCard
    dataPlayers["twoYellowCard"][len(dataPlayers["twoYellowCard"])] = twoYellowCard
    dataPlayers["redCard"][len(dataPlayers["redCard"])] = redCard

dataPlayers_copy = copy.deepcopy(dataPlayers)

# print(dataPlayers)

dataTeams = {"team": dict(), "goals": dict(), "yellowCards": dict(),
             "maxMatches": dict(), "penalties": dict(), "points": dict()}

for currentTeam in dataPlayers["team"].items():
    if currentTeam[1] not in dataTeams["team"].values():
        dataTeams["team"][len(dataTeams["team"])] = currentTeam[1]
        dataTeams["goals"][len(dataTeams["goals"])] = dataPlayers["goals"][currentTeam[0]]
        dataTeams["yellowCards"][len(dataTeams["yellowCards"])] = \
            dataPlayers["yellowCard"][currentTeam[0]] + dataPlayers["twoYellowCard"][currentTeam[0]] * 2
        dataTeams["maxMatches"][len(dataTeams["maxMatches"])] = dataPlayers["matches"][currentTeam[0]]
        dataTeams["penalties"][len(dataTeams["penalties"])] = dataPlayers["penalties"][currentTeam[0]]
    else:
        for teamInDataTeamGoals in dataTeams["team"].items():
            if currentTeam[1] == teamInDataTeamGoals[1]:
                dataTeams["goals"][teamInDataTeamGoals[0]] += dataPlayers["goals"][currentTeam[0]]
                dataTeams["yellowCards"][teamInDataTeamGoals[0]] += \
                    dataPlayers["yellowCard"][currentTeam[0]] + dataPlayers["twoYellowCard"][currentTeam[0]] * 2
                if dataTeams["maxMatches"][teamInDataTeamGoals[0]] < dataPlayers["matches"][currentTeam[0]]:
                    dataTeams["maxMatches"][teamInDataTeamGoals[0]] = dataPlayers["matches"][currentTeam[0]]
                dataTeams["penalties"][teamInDataTeamGoals[0]] += dataPlayers["penalties"][currentTeam[0]]
                break
for team in mainTable.find("tbody").find_all("tr"):
    teamName = team.find("a", attrs={"rel": "nofollow"}).text
    teamMatches = int(team.find("td", attrs={"class": "ctr"}).text)
    for dataTeam in dataTeams["team"].items():
        if teamName == dataTeam[1] and dataTeams["maxMatches"][dataTeam[0]] < teamMatches:
            dataTeams["maxMatches"][dataTeam[0]] = teamMatches
            break
mainTrs = mainTable.find("tbody").find_all("tr")
for currentMainTr in mainTrs:
    currentTeam = currentMainTr.find("a").text
    currentPoints = currentMainTr.find("b").text
    for team in dataTeams["team"].items():
        if currentTeam == team[1]:
            dataTeams["points"][len(dataTeams["points"])] = int(currentPoints)
# for index in range(len(dataTeams["points"]), len(dataTeams["team"])):
#    dataTeams["points"][index] = 0

#print(dataTeams)

headForTable = ["Команда", "ФИ игрока", "Роль", "Голы", "Пенальти", "Пасы", "Матчи", "Штрафные", "Fairy play", "ЖК", "2ЖК", "КК"]
maxLenTeam = len(headForTable[0])
maxLenFI = len(headForTable[1])
maxLenRole = len(headForTable[2])
maxLenGoals = len(headForTable[3])
maxLenPennalties = len(headForTable[4])
maxLenPasses = len(headForTable[5])
maxLenMatches = len(headForTable[6])
maxLenIsPennalties = len(headForTable[7])
maxLenFairyPlay = len(headForTable[8])
maxLenYC = len(headForTable[9])
maxLen2YC = len(headForTable[10])
maxLenRC = len(headForTable[11])

for element in dataPlayers_copy["team"].values():
    if len(element) > maxLenTeam:
        maxLenTeam = len(element)

for element in dataPlayers_copy["player"].values():
    if len(element) > maxLenFI:
        maxLenFI = len(element)

for element in dataPlayers_copy["role"].values():
    if len(element) > maxLenRole:
        maxLenRole = len(element)

while len(headForTable[0]) < maxLenTeam:
    headForTable[0] += " "

while len(headForTable[1]) < maxLenFI:
    headForTable[1] += " "

while len(headForTable[2]) < maxLenRole:
    headForTable[2] += " "

while len(headForTable[7]) < maxLenIsPennalties:
    headForTable[7] += " "

print("Общая таблица игроков")
print("_____________________")

for head in headForTable:
    print(head, end=" | ")
print()
print("________________________________________________________________________________________________________________________________________")

for team in dataPlayers_copy["team"].items():
    while len(dataPlayers_copy["team"][team[0]]) < maxLenTeam:
        dataPlayers_copy["team"][team[0]] += " "
    while len(dataPlayers_copy["player"][team[0]]) < maxLenFI:
        dataPlayers_copy["player"][team[0]] += " "
    while len(dataPlayers_copy["role"][team[0]]) < maxLenRole:
        dataPlayers_copy["role"][team[0]] += " "
    while len(str(dataPlayers_copy["goals"][team[0]])) < maxLenGoals:
        dataPlayers_copy["goals"][team[0]] = str(dataPlayers_copy["goals"][team[0]])
        dataPlayers_copy["goals"][team[0]] += " "
    while len(str(dataPlayers_copy["penalties"][team[0]])) < maxLenPennalties:
        dataPlayers_copy["penalties"][team[0]] = str(dataPlayers_copy["penalties"][team[0]])
        dataPlayers_copy["penalties"][team[0]] += " "
    while len(str(dataPlayers_copy["passes"][team[0]])) < maxLenPasses:
        dataPlayers_copy["passes"][team[0]] = str(dataPlayers_copy["passes"][team[0]])
        dataPlayers_copy["passes"][team[0]] += " "
    while len(str(dataPlayers_copy["matches"][team[0]])) < maxLenMatches:
        dataPlayers_copy["matches"][team[0]] = str(dataPlayers_copy["matches"][team[0]])
        dataPlayers_copy["matches"][team[0]] += " "
    while len(str(dataPlayers_copy["isPenalty"][team[0]])) < maxLenIsPennalties:
        dataPlayers_copy["isPenalty"][team[0]] = str(dataPlayers_copy["isPenalty"][team[0]])
        dataPlayers_copy["isPenalty"][team[0]] += " "
    while len(str(dataPlayers_copy["fairPlay"][team[0]])) < maxLenFairyPlay:
        dataPlayers_copy["fairPlay"][team[0]] = str(dataPlayers_copy["fairPlay"][team[0]])
        dataPlayers_copy["fairPlay"][team[0]] += " "
    while len(str(dataPlayers_copy["yellowCard"][team[0]])) < maxLenYC:
        dataPlayers_copy["yellowCard"][team[0]] = str(dataPlayers_copy["yellowCard"][team[0]])
        dataPlayers_copy["yellowCard"][team[0]] += " "
    while len(str(dataPlayers_copy["twoYellowCard"][team[0]])) < maxLen2YC:
        dataPlayers_copy["twoYellowCard"][team[0]] = str(dataPlayers_copy["twoYellowCard"][team[0]])
        dataPlayers_copy["twoYellowCard"][team[0]] += " "
    while len(str(dataPlayers_copy["redCard"][team[0]])) < maxLenRC:
        dataPlayers_copy["redCard"][team[0]] = str(dataPlayers_copy["redCard"][team[0]])
        dataPlayers_copy["redCard"][team[0]] += " "

    print(dataPlayers_copy["team"][team[0]],
          dataPlayers_copy["player"][team[0]],
          dataPlayers_copy["role"][team[0]],
          dataPlayers_copy["goals"][team[0]],
          dataPlayers_copy["penalties"][team[0]],
          dataPlayers_copy["passes"][team[0]],
          dataPlayers_copy["matches"][team[0]],
          dataPlayers_copy["isPenalty"][team[0]],
          dataPlayers_copy["fairPlay"][team[0]],
          dataPlayers_copy["yellowCard"][team[0]],
          dataPlayers_copy["twoYellowCard"][team[0]],
          dataPlayers_copy["redCard"][team[0]], sep=" | ")

dataTeamsCopyForMaxGoals = copy.deepcopy(dataTeams)
dataTeamsCopyForMaxYellowCards = copy.deepcopy(dataTeams)

# 1)
threeTeamsWithMaxGoals = {"team": dict(), "goals": dict()}
for i in range(3):
    indexMaxGoals = max(dataTeamsCopyForMaxGoals["goals"], key=lambda x: dataTeamsCopyForMaxGoals["goals"][x])
    threeTeamsWithMaxGoals["team"][len(threeTeamsWithMaxGoals["team"])] = \
        dataTeamsCopyForMaxGoals["team"][indexMaxGoals]
    threeTeamsWithMaxGoals["goals"][len(threeTeamsWithMaxGoals["goals"])] = \
        dataTeamsCopyForMaxGoals["goals"][indexMaxGoals]
    del dataTeamsCopyForMaxGoals["team"][indexMaxGoals]
    del dataTeamsCopyForMaxGoals["goals"][indexMaxGoals]
print()
print("1)	Первая тройка команд по числу забитых голов с выводом их числа.")
maxLenTeam = len(headForTable[0])
maxLenGoals = len(headForTable[3])
for element in threeTeamsWithMaxGoals["team"].values():
    if len(element) > maxLenTeam:
        maxLenTeam = len(element)

while len(headForTable[0]) < maxLenTeam:
    headForTable[0] += " "

print(headForTable[0], headForTable[3], sep=" | ")
print("______________________")

for team in threeTeamsWithMaxGoals["team"].items():
    while len(threeTeamsWithMaxGoals["team"][team[0]]) < maxLenTeam:
        threeTeamsWithMaxGoals["team"][team[0]] += " "
    while len(str(threeTeamsWithMaxGoals["goals"][team[0]])) < maxLenGoals:
        threeTeamsWithMaxGoals["goals"][team[0]] = str(threeTeamsWithMaxGoals["goals"][team[0]])
        threeTeamsWithMaxGoals["goals"][team[0]] += " "
    print(threeTeamsWithMaxGoals["team"][team[0]],
          threeTeamsWithMaxGoals["goals"][team[0]],
          sep=" | ")

#print(1, threeTeamsWithMaxGoals)

# 2)
threeTeamsWithMaxYellowCards = {"team": dict(), "yellowCards": dict()}
for i in range(3):
    indexMaxYellowCards = max(dataTeamsCopyForMaxYellowCards["yellowCards"],
                              key=lambda x: dataTeamsCopyForMaxYellowCards["yellowCards"][x])
    threeTeamsWithMaxYellowCards["team"][len(threeTeamsWithMaxYellowCards["team"])] = \
        dataTeamsCopyForMaxYellowCards["team"][indexMaxYellowCards]
    threeTeamsWithMaxYellowCards["yellowCards"][len(threeTeamsWithMaxYellowCards["yellowCards"])] = \
        dataTeamsCopyForMaxYellowCards["yellowCards"][indexMaxYellowCards]
    del dataTeamsCopyForMaxYellowCards["team"][indexMaxYellowCards]
    del dataTeamsCopyForMaxYellowCards["yellowCards"][indexMaxYellowCards]
#print(2, threeTeamsWithMaxYellowCards)

print()
print("2)	Первая тройка команд по числу желтых карточек.")
maxLenTeam = len(headForTable[0])
maxLenYC = len(headForTable[9])
for element in threeTeamsWithMaxYellowCards["team"].values():
    if len(element) > maxLenTeam:
        maxLenTeam = len(element)

while len(headForTable[0]) < maxLenTeam:
    headForTable[0] += " "

print(headForTable[0], headForTable[9], sep=" | ")
print("______________________")

for team in threeTeamsWithMaxYellowCards["team"].items():
    while len(threeTeamsWithMaxYellowCards["team"][team[0]]) < maxLenTeam:
        threeTeamsWithMaxYellowCards["team"][team[0]] += " "
    while len(str(threeTeamsWithMaxYellowCards["yellowCards"][team[0]])) < maxLenYC:
        threeTeamsWithMaxYellowCards["yellowCards"][team[0]] = str(threeTeamsWithMaxYellowCards["yellowCards"][team[0]])
        threeTeamsWithMaxYellowCards["yellowCards"][team[0]] += " "
    print(threeTeamsWithMaxYellowCards["team"][team[0]],
          threeTeamsWithMaxYellowCards["yellowCards"][team[0]],
          sep=" | ")

# 3)
playersWhoDontPlayInAllMatches = {"players": dict(), "matches": dict(), "maxMatches": dict()}
for team in dataTeams["team"].items():
    for teamOfPlayer in dataPlayers["team"].items():
        if (team[1] == teamOfPlayer[1]) and \
                (dataTeams["maxMatches"][team[0]] > dataPlayers["matches"][teamOfPlayer[0]]):
            playersWhoDontPlayInAllMatches["players"][len(playersWhoDontPlayInAllMatches["players"])] = \
                dataPlayers["player"][teamOfPlayer[0]]
            playersWhoDontPlayInAllMatches["matches"][len(playersWhoDontPlayInAllMatches["matches"])] = dataPlayers["matches"][teamOfPlayer[0]]
            playersWhoDontPlayInAllMatches["maxMatches"][len(playersWhoDontPlayInAllMatches["maxMatches"])] = dataTeams["maxMatches"][team[0]]
#print(3, playersWhoDontPlayInAllMatches)

print()
print("3)	Список игроков, которые участвовали не во всех играх своей команды. ")

for player in playersWhoDontPlayInAllMatches["players"].items():
    print(playersWhoDontPlayInAllMatches["players"][player[0]], " ", str(playersWhoDontPlayInAllMatches["matches"][player[0]]) + "/" + str(playersWhoDontPlayInAllMatches["maxMatches"][player[0]]))


# 4)
teamsAndProportionOfPenalties = {"team": dict(), "proportionOfPenalties": dict()}
for team in dataTeams["team"].items():
    teamsAndProportionOfPenalties["team"][len(teamsAndProportionOfPenalties["team"])] = team[1]
    if dataTeams["goals"][team[0]] != 0:
        teamsAndProportionOfPenalties["proportionOfPenalties"][
            len(teamsAndProportionOfPenalties["proportionOfPenalties"])] = \
            round(dataTeams["penalties"][team[0]] / dataTeams["goals"][team[0]], 2)
    else:
        teamsAndProportionOfPenalties["proportionOfPenalties"][
            len(teamsAndProportionOfPenalties["proportionOfPenalties"])] = 0
#print(4, teamsAndProportionOfPenalties)

print()
print("4)	Доля пенальти по отношению к числу голов для каждой команды.")
maxLenTeam = len(headForTable[0])
print(headForTable[0], "Доля пенальти от голов", sep=" | ")

for team in teamsAndProportionOfPenalties["team"].values():
    if len(team) > maxLenTeam:
        maxLenTeam = len(team)

for team in teamsAndProportionOfPenalties["team"].items():
    while len(teamsAndProportionOfPenalties["team"][team[0]]) < maxLenTeam:
        teamsAndProportionOfPenalties["team"][team[0]] += " "
    teamsAndProportionOfPenalties["proportionOfPenalties"][team[0]] = float(teamsAndProportionOfPenalties["proportionOfPenalties"][team[0]])
    print(teamsAndProportionOfPenalties["team"][team[0]],
          teamsAndProportionOfPenalties["proportionOfPenalties"][team[0]],
          sep=" | ")


# 5)
print()
print("5)	Корреляция числа голов с количеством очков команды. ")
corrCoefGoalsAndPoints = numpy.corrcoef(list(dataTeams["goals"].values()), list(dataTeams["points"].values()))
#print(list(dataTeams["goals"].values()))
#print(list(dataTeams["points"].values()))
print(round(corrCoefGoalsAndPoints[0][1], 2))
