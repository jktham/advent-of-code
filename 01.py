with open(r".\data\01.txt") as file:
    data = file.read()

data = data.split("\n")
data = [int(scan) for scan in data]

# part 1
increase_count = 0
for i in range(len(data)):
    if data[i] > data[i-1] and i > 0:
        increase_count += 1

print(increase_count)

# part 2
scan_sum = [0] * len(data)
for i in range(len(data)):
    if i > 2:
        scan_sum[i] = data[i] + data[i-1] + data[i-2]

sum_increase_count = 0
for i in range(len(scan_sum)):
    if scan_sum[i] > scan_sum[i-1] and i > 0:
        sum_increase_count += 1

print(sum_increase_count)