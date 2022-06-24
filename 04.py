with open(r".\data\04.txt") as file:
    data = file.read()

data = data.split("\n")
data.append("")

numbers = data[0].split(",")

class Board:
    def __init__(self, values, marked):
        self.values = values
        self.marked = marked

boards = []
for i in range(2, len(data)):
    if data[i] == "":
        boards.append(Board([row.split() for row in data[i-5:i]], [[0]*5 for _ in range(5)]))

def checkWin(i):
    for j in range(5):
        if sum(boards[i].marked[j]) == 5:
            return True
    for j in range(5):
        if sum([row[j] for row in boards[i].marked]) == 5:
            return True

def calculateScore(i, n):
    score = 0
    for j in range(5):
        for k in range(5):
            if boards[i].marked[j][k] == 0:
                score += int(boards[i].values[j][k])
    return score * int(n)

def drawNumbers(numbers):
    scores = []
    winners = []
    for n in numbers:
        for i in range(len(boards)):
            for j in range(5):
                for k in range(5):
                    if int(boards[i].values[j][k]) == int(n):
                        boards[i].marked[j][k] = 1 
            if checkWin(i) and i not in winners:
                score = calculateScore(i, n)
                scores.append(score)
                winners.append(i)
    return scores

scores = drawNumbers(numbers)

print(scores[0])
print(scores[-1])