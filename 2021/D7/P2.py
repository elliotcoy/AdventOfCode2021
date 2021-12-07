
crabs = list(map(int,open('2021\D7\input.txt','r').read().split(',')))

def abs(n):
    if n < 0:
        return n*-1
    return n

def sumcount(n):
    return int(n*(n+1)/2)

bestCost = -1
bestx = -1

for xpos in range(min(crabs), max(crabs)):

    cost = 0
    for x in crabs:
        steps = abs(x-xpos)
        cost += sumcount(steps)
    
    if cost < bestCost or bestCost < 0:
        bestCost = cost
        bestx = xpos
        
    
print(f'x: {bestx}') ; print(f'fuel: {bestCost}')