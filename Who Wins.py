def TakeTurn(h1,h2,h3,player):
    if h1+h2+h3<=1:
        return -1*player

    result=[]
    for s in range(h1,0,-1):
        result.append(TakeTurn(h1-s,h2,h3,-1*player))

    for s in range(h2,0,-1):
        result.append(TakeTurn(h1,h2-s,h3,-1*player))

    for s in range(h3,0,-1):
        result.append(TakeTurn(h1,h2,h3-s,-1*player))

    if player==1:
        return max(result)
    else:
        return min(result)

print(TakeTurn(4,4,4,1))
#https://brilliant.org/daily-problems/3-heaps-nim/