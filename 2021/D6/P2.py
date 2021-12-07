
fishlist = list(map(int, open('2021\D6\input.txt','r').read().split(',') ))
print(fishlist)

days = 256
numfish = []
numfish.append([0]*7) # old fish 0 -> 6
numfish.append([0]*2) # new fish 0 -> 1
out = 0

for fish in fishlist:
    numfish[0][fish] += 1

for day in range(days):

    temp = [0]*7

    for i in range(7): 
        temp[i-1] = numfish[0][i]

    temp[6] += numfish[1][0]
    numfish[1][0] = numfish[1][1]
    numfish[1][1] = numfish[0][0]

    numfish[0] = temp

    # update total number of fish
    out = 0
    for count in numfish[0]:  out += count
    for count in numfish[1]:  out += count

    print(f'D{day+1}:  {out}')

