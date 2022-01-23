with open(r".\data\7.txt") as file:
    data = file.read()

data = [int(num) for num in data.split(",")]

average = sum(data)/len(data)

# part 1
def linearCost(data):
    fuel = []
    for i in range(max(data)):
        cost = 0
        for j in range(len(data)):
            cost += abs(i - data[j])
        fuel.append(cost)
    return min(fuel)

print(linearCost(data))

# part 2
def gaussCost(data):
    fuel = []
    for i in range(max(data)):
        cost = 0
        for j in range(len(data)):
            cost += int(abs(i - data[j])*(abs(i - data[j])+1)/2)
        fuel.append(cost)
    return min(fuel)

print(gaussCost(data))