with open(r".\data\06.txt") as file:
    data = file.read()

data = [int(num) for num in data.split(",")]

# part 1
def simulate(fishes, days):
    for _ in range(days):
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 7
                fishes.append(8)
            fishes[i] -= 1
    return len(fishes)

print(simulate(data[:], 80))

# part 2
def simulateOptimized(fishes, days):
    count = [0]*9
    for i in range(9):
        count[i] = fishes.count(i)
    
    for _ in range(days):
        new = count[0]
        for i in range(1, 9):
            count[i-1] = count[i]
        count[6] += new
        count[8] = new
    return sum(count)

print(simulateOptimized(data[:], 256))