from typing import Match

out = 0
x = 0
y = 0
a = 0

with open('Day 2\P1\input.txt', 'r') as s:
    for line in s:
        cmd = line.split(' ')
        
        if cmd[0]=='forward':
            x += int(cmd[1])
            y += int(cmd[1])*a
        elif cmd[0]=='down':
            a += int(cmd[1])
        else:
            a -= int(cmd[1])
            
out = x*y
print(out)
