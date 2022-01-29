with open(r".\data\3.txt") as file:
    data = file.read()

data = data.split("\n")

# part 1
def getMostCommonBits(data):
    bit_sum = [0] * len(data[0])
    for i in range(len(data)):
        for j in range(len(data[0])):
            bit_sum[j] += int(data[i][j])

    bits = ""
    for i in range(len(data[0])):
        if bit_sum[i] >= len(data)/2:
            bits += "1"
        else:
            bits += "0"
    return bits

gamma_rate = int("".join(getMostCommonBits(data)), 2)
epsilon_rate = 2**len(data[0])-1 - gamma_rate

print(gamma_rate*epsilon_rate)

# part 2
o2_data = data[:]
for i in range(len(data[0])):
    most_common_bits = getMostCommonBits(o2_data)
    for j in range(len(data)):
        if len(o2_data) == 1:
            break
        elif data[j][i] != most_common_bits[i] and data[j] in o2_data:
            o2_data.remove(data[j])
o2_rating = int(o2_data[0], 2)

co2_data = data[:]
for i in range(len(data[0])):
    most_common_bits = getMostCommonBits(co2_data)
    for j in range(len(data)):
        if len(co2_data) == 1:
            break
        elif data[j][i] == most_common_bits[i] and data[j] in co2_data:
            co2_data.remove(data[j])
co2_rating = int(co2_data[0], 2)

print(o2_rating*co2_rating)
