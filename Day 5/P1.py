
# handle input
inList = open('Day 5\input.txt', 'r').read().splitlines()

# vec2 exists now
class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

# basic sign function (-1, 0, 1)
def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0

fr = []
to = []
for line in inList:
    # split from/to
    fromto = line.split(' -> ')
    # get x,y lists
    a1 = list(map(int, fromto[0].split(',')))
    a2 = list(map(int, fromto[1].split(',')))
    # convert to vec2
    p1 = vec2(a1[0],a1[1])
    p2 = vec2(a2[0],a2[1])
    # add to fr/to
    fr.append(p1)
    to.append(p2)

# input handled, wokring


# make the grid
grid = [ [0]*1000 for _ in range(1000) ]

for i in range(len(fr)):
    p1 = fr[i]
    p2 = to[i]
    
    dx = sign(p2.x-p1.x)
    dy = sign(p2.y-p1.y)
        
    if(dx!=0 and dy!=0):
        print('..........SKIP')
        continue
    
    #add start point to grid
    grid[p1.x][p1.y] += 1
    
    while str(p1) != str(p2):
        # traverse line
        p1.x += dx
        p1.y += dy
        
        # add point to grid
        grid[p1.x][p1.y] += 1
        
        # recheck direction
        dx = sign(p2.x-p1.x)
        dy = sign(p2.y-p1.y)

def drawGrid(_g):
    for i in range(len(_g)):
        rowString = ''
        for j in range(len(_g[i])):
            n = _g[j][i]
            if n==0:
                rowString += '.'
            else:
                rowString += str(n)
        print(rowString)
    return 0

drawGrid(grid)

overlaps = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1: 
            overlaps += 1
        
print(overlaps)
