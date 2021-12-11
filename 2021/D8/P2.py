
file = open('2021\D8\input.txt','r').read().splitlines()
s = []

mapcode = { 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', 'f':'', 'g':'' }

wirecode = {
    0:'',
    1:'',
    2:'',
    3:'',
    4:'',
    5:'',
    6:'',
    7:'',
    8:'',
    9:''
}
numcode = {
    0:'abcefg',
    1:'cf',
    2:'acdeg',
    3:'acdfg',
    4:'bcdf',
    5:'abdfg',
    6:'abdefg',
    7:'acf',
    8:'abcdefg',
    9:'abcdfg'
}

for line in file:
    s.append(line.split('|')[1].split())

out = 0
for a in s:
    for i in a:
        l = len(i)
        if l==2 or l==3 or l==4 or l==7:
            out += 1

print(out)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["brand"] = "no"
print(thisdict["brand"])