
fishlist = list(map(int, open('Day 6\input.txt','r').read().split(',') ))
print(fishlist)

# TODO: add grouping for larger number of days.

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
        
    print(f'Day {day}:  ' + str(len(fishlist)))

print(len(fishlist))

