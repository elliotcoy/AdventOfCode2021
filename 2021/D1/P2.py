s =  open('2021\D1\input.txt', 'r').read()
list = [int(x) for x in s.splitlines()]
out = 0

for i in range(len(list)-2):
    if i > 0:
        a = list[i-1] + list[i] + list[i+1]
        b = list[i] + list[i+1] + list[i+2]
        if b > a:
            out += 1

print(out)
