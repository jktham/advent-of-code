with open(r".\data\10.txt") as file:
    data = file.read()

data = data.split("\n")

# part 1
symbols_open = ["(", "[", "{", "<"]
symbols_close = [")", "]", "}", ">"]
symbols_error_value = {")":3, "]":57, "}":1197, ">":25137}

error_score = 0
corrupted_lines = []
for i in range(len(data)):
    nest = []
    for j in range(len(data[i])):
        if data[i][j] in symbols_open:
            nest.append(data[i][j])

        elif data[i][j] in symbols_close:
            if nest[-1] == symbols_open[symbols_close.index(data[i][j])]:
                nest.pop()
            else:
                error_score += symbols_error_value.get(data[i][j])
                corrupted_lines.append(i)
                break

print(error_score)

# part 2
for i in corrupted_lines[::-1]:
    data.pop(i)

completion_scores = []
for i in range(len(data)):
    nest = []
    score = 0
    for j in range(len(data[i])):
        if data[i][j] in symbols_open:
            nest.append(data[i][j])

        elif data[i][j] in symbols_close:
            if nest[-1] == symbols_open[symbols_close.index(data[i][j])]:
                nest.pop()
    
    for j in range(len(nest)):
        score = score * 5 + symbols_open.index(nest[-j-1]) + 1
    completion_scores.append(score)

completion_scores.sort()
print(completion_scores[int((len(completion_scores)-1)/2)])
