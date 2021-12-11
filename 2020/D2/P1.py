
inputlist = open('2020\D2\input.txt','r').read().split()

minmax = []
char = []
pw = []

for i in range(0, len(inputlist), 3):
    minmax.append( list(map(int, inputlist[i].split('-'))) )
    char.append( inputlist[i+1][0] )
    pw.append( inputlist[i+2] )
    
for i in range(len(pw)):
    print(pw[i])
    # start checking chars