out = 0
lineWidth = 12
inputList = open('Day 3\input.txt', 'r').read().splitlines()

# common bit from column
def comBit(_list, _i):
    c0 = 0
    c1 = 0
    for line in _list:
        bit = line[_i]
        if bit == '1':
            c1 += 1
        else:
            c0 += 1
    if c1<c0:
        return '0'
    else:
        return '1'

# uncommon bit from column
def unBit(_list, _i):
    if comBit(_list, _i)=='1':
        return '0'
    else:
        return '1'

# oxygen generator rating
oxyList = inputList
for i in range(lineWidth):
    tempList = []
    cb = comBit(oxyList, i)
    for line in oxyList:
        if line[i] == cb:
            tempList.append(line)
    oxyList = tempList
    if len(oxyList) == 1:
        break

# co2 scrubber rating
co2List = inputList
for i in range(lineWidth):
    tempList = []
    cb = unBit(co2List, i)
    for line in co2List:
        if line[i] == cb:
            tempList.append(line)
    co2List = tempList
    if len(co2List) == 1:
        break

oxy = int(oxyList[0], 2)
co2 = int(co2List[0], 2)
out = co2*oxy

print(out)
