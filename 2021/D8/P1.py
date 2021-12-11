
file = open('2021\D8\input.txt','r').read().splitlines()
s = []

for line in file:
    s.append(line.split('|')[1].split())

out = 0
for a in s:
    for i in a:
        l = len(i)
        if l==2 or l==3 or l==4 or l==7:
            out += 1

print(out)
