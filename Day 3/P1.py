out = 0
gamma = ''
epsilon = ''
bits = [0] * 12
file = open('Day 3\input.txt', 'r')


for line in file:
    for i in range(12):
        b = int(line[i])
        bits[i] += b*2-1

for i in range(len(bits)):
    if bits[i] > 0:
        gamma += str(1)
        epsilon += str(0)
    else:
        gamma += str(0)
        epsilon += str(1)

out = str(int(gamma, 2) * int(epsilon, 2))

print(out)
