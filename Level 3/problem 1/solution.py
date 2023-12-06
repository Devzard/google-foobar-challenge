def pattern_xor(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0
        
        
def solution(start, length):
    ans = 0
    
    for i in range(length):
        rstart = start + (i * length)
        rend = rstart + (length - 1 - i)
        ans ^= pattern_xor(rend) ^ pattern_xor(rstart - 1)
        
    return ans

print("ans :", solution(17, 4))
print("ans :", solution(0, 3))
# print("ans :", solution(2000000000, 100000))
