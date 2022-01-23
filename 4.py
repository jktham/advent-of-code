import copy

with open(r".\data\4.txt") as file:
    data = file.read()

data = data.split("\n")
data.append("")

drawn = data[0].split(",")

boards = []
for i in range(2, len(data)):
    if data[i] == "":
        boards.append([row.split() for row in data[i-5:i]])

def checkWin(i):
    for j in range(len(boards[0])):
        if sum(marked[i][j]) == 5:
            return True
    for j in range(len(boards[0][0])):
        if sum([row[j] for row in marked[i]]) == 5:
            return True

def calculateScore(i, n):
    score = 0
    for j in range(len(boards[0])):
        for k in range(len(boards[0][0])):
            if marked[i][j][k] == 0:
                score += int(boards[i][j][k])
    return score * int(n)

marked = copy.deepcopy(boards)
for i in range(len(boards)):
    for j in range(len(boards[0])):
        for k in range(len(boards[0][0])):
            marked[i][j][k] = 0

stop = False
scores = []
for n in drawn:
    if stop:
        break
    for i in range(len(boards)):
        for j in range(len(boards[0])):
            for k in range(len(boards[0][0])):
                if int(boards[i][j][k]) == int(n):
                    marked[i][j][k] = 1
        if checkWin(i):
            score = calculateScore(i, n)
            scores.append(score)

print(scores[0])
print(scores)