def solution(M, F):
    m = int(M)
    f = int(F)
    count = 0
    while m > 1 or f > 1:
        if m < 1 or f < 1:
            return "impossible"
        if m == f:
            return "impossible"
        if m > f:
            count += m // f
            m = m % f
        else:
            count += f // m
            f = f % m
    return str(count - 1)


print(solution('4', '7'))
print(solution('2', '1'))
print(solution('2', '4'))