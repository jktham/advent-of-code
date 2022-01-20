with open(r".\data\3.txt") as file:
    data = file.read()

data = data.split("\n")

# part 1
bit_sum = [0] * len(data[0])
for i in range(len(data)):
    for j in range(len(data[0])):
        bit_sum[j] += int(data[i][j])

binary_gamma_rate = ""
for i in range(len(data[0])):
    if bit_sum[i] > len(data)/2:
        binary_gamma_rate += "1"
    else:
        binary_gamma_rate += "0"

gamma_rate = int("".join(binary_gamma_rate), 2)
epsilon_rate = 2**len(data[0])-1 - gamma_rate

print(gamma_rate*epsilon_rate)

# part 2
