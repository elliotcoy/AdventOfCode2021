
L = list(map(int,open('2020\D1\input.txt', 'r').read().split()))

print(L)

def isSum2020(n):
    if sum(n) == 2020:
        return True
    return False


for i in range(len(L)):
    for j in range(len(L)):
        for k in range(len(L)):
            if i==j or i==k or j==k:
                continue
            if isSum2020( [L[i], L[j], L[k]]):
                print(L[i] * L[j] * L[k])

