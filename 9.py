from numpy import size


with open(r".\data\9.txt") as file:
    data = file.read()

data = [[int(num) for num in str(row)] for row in data.split("\n")]

# part 1
def checkLowPoint(data, x, y):
    neighbors = []
    if x > 0:
        neighbors.append(data[x-1][y])
    if x < len(data)-1:
        neighbors.append(data[x+1][y])
    if y > 0:
        neighbors.append(data[x][y-1])
    if y < len(data[0])-1:
        neighbors.append(data[x][y+1])
    
    if neighbors and min(neighbors) > data[x][y]:
        return True

risk = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if checkLowPoint(data, i, j):
            risk += data[i][j] + 1

print(risk)

# part 2
class BasinNode:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

def exploreBasin(data, x, y):
    queue = []
    found = []
    queue.append(BasinNode((x, y)))
    while queue:
        node = queue[0]
        queue.pop(0)
        if data[node.x][node.y] < 9 and (node.x, node.y) not in found:
            found.append((node.x, node.y))
            if node.x > 0:
                queue.append(BasinNode((node.x-1, node.y)))
            if node.x < len(data)-1:
                queue.append(BasinNode((node.x+1, node.y)))
            if node.y > 0:
                queue.append(BasinNode((node.x, node.y-1)))
            if node.y < len(data[0])-1:
                queue.append(BasinNode((node.x, node.y+1)))
    return len(found)

lowpoints = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if checkLowPoint(data, i, j):
            lowpoints.append((i, j))

sizes = []
for i in range(len(lowpoints)):
    sizes.append(exploreBasin(data, lowpoints[i][0], lowpoints[i][1]))
sizes.sort()

print(sizes[-1]*sizes[-2]*sizes[-3])