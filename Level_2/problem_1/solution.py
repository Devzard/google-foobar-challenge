from collections import deque

def getAllPossibleSquares(src):
    lineNo, indexInLine = divmod(src, 8)
    
    # 0 -> lineNo, 1, 2 -> indexInLine
    directions = [[-2, -1, +1], [-1, -2, +2], [+1, -2, +2], [+2, -1, +1]]
    
    possibleSquares = []
    for direction in directions:
        newLine = lineNo + direction[0]
        if newLine >= 0 and newLine < 8:
            newIndex = indexInLine + direction[1]
            if newIndex >= 0 and newIndex < 8:
                possibleSquares.append(newLine * 8 + newIndex)
            newIndex = indexInLine + direction[2]
            if newIndex >= 0 and newIndex < 8:
                possibleSquares.append(newLine * 8 + newIndex)
                
    return possibleSquares

def solution(src, dest):
    visited = [False] * 64
    q = deque([(src, 0)])
    
    while q:
        square, level = q.popleft()
        if square == dest:
            return level
        
        for nextSquare in getAllPossibleSquares(square):
            if not visited[nextSquare]:
                visited[nextSquare] = True
                q.append((nextSquare, level + 1))
                
    return -1

print(solution(0, 36))
