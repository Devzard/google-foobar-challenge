def traverse(node, height, level, index, arr):
    if level > height:
        return index

    left = 2 * node + 1
    right = 2 * node + 2

    left_idx = traverse(left, height, level + 1, index, arr)
    right_idx = traverse(right, height, level + 1, left_idx, arr)

    arr[node] = right_idx + 1
    
    return right_idx + 1

def solution(h, q):
    arr = [-1] * (2 ** h - 1)
    p = []
    traverse(0, h, 1, 0, arr)
    for item in q:
        child = arr.index(item)
        if child == 0:
            p.append(-1)
            continue
        elif child % 2 == 0:
            parent = (child - 2) // 2
        else:
            parent = (child - 1) // 2
        p.append(arr[parent])
    return p

print(solution(3, [1, 4, 7]))
print(solution(3, [7, 3, 5, 1]))
print(solution(5, [19, 14, 28]))