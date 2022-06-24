with open(r".\data\08.txt") as file:
    data = file.read()

data = [[[set(word) for word in cell.split(" ")] for cell in row.split(" | ")] for row in data.split("\n")]

# part 1
count = [0]*10
for i in range(len(data)):
    for j in range(len(data[i][1])):
        if len(data[i][1][j]) == 2:
            count[1] += 1
        elif len(data[i][1][j]) == 4:
            count[4] += 1
        elif len(data[i][1][j]) == 3:
            count[7] += 1
        elif len(data[i][1][j]) == 7:
            count[8] += 1

print(sum(count))

# part 2
output = 0
for i in range(len(data)):
    segments = [{}]*10
    for j in range(len(data[i])):
        for k in range(len(data[i][j])):
            if len(data[i][j][k]) == 2:
                segments[1] = data[i][j][k]
            elif len(data[i][j][k]) == 4:
                segments[4] = data[i][j][k]
            elif len(data[i][j][k]) == 3:
                segments[7] = data[i][j][k]
            elif len(data[i][j][k]) == 7:
                segments[8] = data[i][j][k]

    for j in range(len(data[i])):
        for k in range(len(data[i][j])):
            if len(data[i][j][k]) == 5 and segments[1] < data[i][j][k]:
                segments[3] = data[i][j][k]
            elif len(data[i][j][k]) == 6 and segments[4] < data[i][j][k]:
                segments[9] = data[i][j][k]
            elif len(data[i][j][k]) == 6 and not segments[7] < data[i][j][k]:
                segments[6] = data[i][j][k]
            elif len(data[i][j][k]) == 6 and segments[7] < data[i][j][k] and not segments[4] < data[i][j][k]:
                segments[0] = data[i][j][k]
    
    for j in range(len(data[i])):
        for k in range(len(data[i][j])):
            if len(data[i][j][k]) == 5 and len(segments[9] ^ data[i][j][k]) == 1 and not segments[1] < data[i][j][k]:
                segments[5] = data[i][j][k]
            elif len(data[i][j][k]) == 5 and len(segments[9] ^ data[i][j][k]) == 3:
                segments[2] = data[i][j][k]

    digits = ""
    for j in range(len(data[i][1])):
        for k in range(10):
            if data[i][1][j] == segments[k]:
                digits += str(k)

    output += int(digits)

print(output)