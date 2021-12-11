
inputlist = open('2021\D9\input.txt','r').read().splitlines()[::1]
s=[]
for line in inputlist:
    newline=[]
    for char in line:
        newline.append(int(char))
    s.append(newline)

lowpoints = []

for i in range(len(s)):
    for j in range(len(s[i])):
        n = s[i][j]
        
        #check left
        if i!=0 and s[i-1][j] <= n: continue
        #check right
        if i!=len(s)-1 and s[i+1][j] <= n: continue
        #check up
        if j!=0 and s[i][j-1] <= n: continue
        #check down
        if j!=len(s[i])-1 and s[i][j+1] <= n: continue
        
        lowpoints.append(s[i][j]+1)
        print(f'lowpoint found at [{j},{i}] = {s[i][j]}')

print(sum(lowpoints))