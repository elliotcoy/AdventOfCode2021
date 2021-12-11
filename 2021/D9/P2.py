
inputlist = open('2021\D9\input.txt','r').read().splitlines()[::1]

s=[]
b = 0

for line in inputlist:
    newline=[]
    for char in line:
        newline.append(int(char))
    s.append(newline)

def getBasin(i, j):
    if s[i][j] == 9:
        return 0

    for x in range(5):
        p = ''
        for y in range(10):
            if x==i and y==j:
                p+='*'
            else:
                p+=str(s[x][y])
                
    s[i][j] = 9
    b = 1
    
    if i!=0:            b += getBasin(i-1, j)
    if i!=len(s)-1:     b += getBasin(i+1, j)
    if j!=0:            b += getBasin(i, j-1)
    if j!=len(s[i])-1:  b += getBasin(i, j+1)

    return b
    
    
basins = []

for i in range(len(s)):
    for j in range(len(s[i])):
        n = s[i][j]
        
        basin = getBasin(i, j)
        if basin > 0:
            basins.append(basin)

out = [0,0,0]
for basin in basins:
    out.append(basin)
    out.remove(min(out))

print(out)
print(out[0]*out[1]*out[2])
