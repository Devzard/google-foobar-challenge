import math

def findSquares(area, res):
    if area == 1:
        res.append(1)
        return res
    elif area == 0:
        return res
    
    sq = int(math.floor(math.sqrt(area)))
    temp = sq**2
    area -= temp
    res.append(temp)
    return findSquares(area, res)
    

def solution(area):
    return findSquares(area, [])

print(solution(15))
