
L = list(map(int,open('2020\D1\input.txt', 'r').read().split()))

print(L)

def isSum2020(n, m):
    if n+m == 2020:
        return True
    return False

for i in range(len(L)):
    for j in range(len(L)):
        if i==j:
            continue
        if isSum2020(L[i], L[j]):
            print(L[i] * L[j])
