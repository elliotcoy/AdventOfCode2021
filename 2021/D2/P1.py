out = 0
x = 0
y = 0

with open('2021\D2\P1\input.txt', 'r') as s:
    for line in s:
        cmd = line.split(' ')
        
        if cmd[0]=='forward':   x += int(cmd[1])
        elif cmd[0]=='down':    y += int(cmd[1])
        else:                   y -= int(cmd[1])
            
out = x*y
print(out)
