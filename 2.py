with open(r".\data\2.txt") as file:
    data = file.read()

data = data.split("\n")
data = [step.split(" ") for step in data]
data = [[step[0], int(step[1])] for step in data]

# part 1
depth = 0
position = 0
for i in range(len(data)):
    if data[i][0] == "up":
        depth -= data[i][1]
    elif data[i][0] == "down":
        depth += data[i][1]
    elif data[i][0] == "forward":
        position += data[i][1]

print(position*depth)

# part 2
depth = 0
position = 0
aim = 0
for i in range(len(data)):
    if data[i][0] == "up":
        aim -= data[i][1]
    elif data[i][0] == "down":
        aim += data[i][1]
    elif data[i][0] == "forward":
        position += data[i][1]
        depth += aim * data[i][1]

print(position*depth)