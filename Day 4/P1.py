from copy import deepcopy

# Input
inputList = open('Day 4\input.txt', 'r').read().splitlines()

# Numbers to be drawn
drawList = inputList[0].split(',')

# Scorecards in play
cardList = []
for i in range(2, len(inputList), 6):
    card = []
    for j in range(5):
        card.append([])
        for k in range(5):
            card[j].append( int(inputList[i+j].split()[k]) )
    cardList.append(card)

# Marks on scorecards   
bingoList = deepcopy(cardList)
for i in range(len(bingoList)):
    for j in range(5):
        for k in range(5):
            bingoList[i][j][k] = 0
            
winnersIndex = []

def bingoCheck(card):
    for i in range(5):
        row = 0
        col = 0
        for j in range(5):
            row += card[i][j]
            col += card[j][i]
        if row == 5 or col == 5:
            return True
    return False


winnerIndex = -1
lastNumberDrawn = -1

bingo = False
for d in range(len(drawList)):
    if bingo: break
    
    for i in range(len(cardList)):
        if bingo: break
        
        for row in range(5):
            for col in range(5):
                if cardList[i][row][col] == int(drawList[d]):
                    bingoList[i][row][col] = 1
                    
        if bingoCheck(bingoList[i]) == True:
            winnerIndex = i
            lastNumberDrawn = int(drawList[d])
            print(str(i)+' is bingo')
            bingo=True
            
def countScore(_card, _cardMarks):
    score = 0
    for i in range(5):
        for j in range(5):
            if _cardMarks[i][j] == 0:
                score += _card[i][j]
    return score

out = countScore(cardList[winnerIndex], bingoList[winnerIndex]) * lastNumberDrawn
print(out)
