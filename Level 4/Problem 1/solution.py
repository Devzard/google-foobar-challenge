import math

def solution(dimensions, your_position, guard_position, distance):
    max_x = your_position[0] + distance
    max_y = your_position[1] + distance

    mirror_x = math.ceil(max_x / dimensions[0])
    mirror_y = math.ceil(max_y / dimensions[1])

    pos_in_first_quadrant = []
    for x in range(mirror_x + 1):
        mirror_x_pos = x * dimensions[0]

    print(pos_in_first_quadrant)

    return 0


print(solution([3, 2], [1, 1], [2, 1], 4))