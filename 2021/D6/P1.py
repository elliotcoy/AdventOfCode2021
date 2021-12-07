
fishlist = list(map(int, open('2021\D6\input.txt','r').read().split(',') ))
print(fishlist)

days = 80
for day in range(days):
    newfish = 0
    for n in range(len(fishlist)):
        fishlist[n] -= 1
        if fishlist[n] < 0:
            fishlist[n] = 6
            newfish += 1

    for i in range(newfish):
        fishlist.append(8)
        
    print(f'D{day}:  ' + str(len(fishlist)))

print(len(fishlist))

