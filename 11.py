with open(r".\data\11.txt") as file:
    data = file.read()

data = [[int(num) for num in str(row)] for row in data.split("\n")]

# part 1
def flash(data, flashing, flash_count):
    flashed = []

    if flashing:
        for co in flashing:
            if co not in flashed:

                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if co[0]+x >= 0 and co[0]+x < len(data) and co[1]+y >= 0 and co[1]+y < len(data[0]):
                            data[co[0]+x][co[1]+y] += 1
                data[co[0]][co[1]] -= 1
            
                flashed.append(co)
                flash_count += 1
                
                for i in range(len(data)):
                    for j in range(len(data[i])):
                        if data[i][j] > 9 and [i, j] not in flashing:
                            flashing.append([i, j])

    for co in flashed:
        data[co[0]][co[1]] = 0

    return data, flash_count

def simulate(data, steps):
    data = [list(row) for row in data]
    flash_count = 0

    for s in range(steps):
        flashing = []

        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1
                if data[i][j] > 9:
                    flashing.append([i, j])

        data, flash_count = flash(data, flashing, flash_count)
            
    return data, flash_count

print(simulate(data, 100)[1])

# part 2
def findSync(data):
    data = [list(row) for row in data]
    sync = False
    n = 0

    while not sync:
        n += 1
        data = simulate(data, 1)[0]
        
        if sum([sum(row) for row in data]) == 0:
            sync = True

    return n

print(findSync(data))