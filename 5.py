with open(r".\data\5.txt") as file:
    data = file.read()

data = data.split("\n")
data = [[[int(num) for num in pair.split(",")] for pair in row.split(" -> ")] for row in data]

class Line:
    def __init__(self, start, end):
        self.x1 = start[0]
        self.y1 = start[1]
        self.x2 = end[0]
        self.y2 = end[1]

lines = []
for i in range(len(data)):
    lines.append(Line(data[i][0], data[i][1]))

horizontal_layered_lines = [[0]*1000 for _ in range(1000)]
layered_lines = [[0]*1000 for _ in range(1000)]
for line in lines:
    dx = 1
    dy = 1
    if line.x1 > line.x2:
        dx = -1
    if line.y1 > line.y2:
        dy = -1
        
    if line.x1 == line.x2 or line.y1 == line.y2:
        for x in range(line.x1, line.x2+dx, dx):
            for y in range(line.y1, line.y2+dy, dy):
                horizontal_layered_lines[x][y] += 1
                layered_lines[x][y] += 1
    else:
        for x, y in zip(range(line.x1, line.x2+dx, dx), range(line.y1, line.y2+dy, dy)):
            layered_lines[x][y] += 1
        
horizontal_count = 0
count = 0
for x in range(len(layered_lines)):
    for y in range(len(layered_lines[0])):
        if horizontal_layered_lines[x][y] > 1:
            horizontal_count += 1
        if layered_lines[x][y] > 1:
            count += 1
            
print(horizontal_count)
print(count)