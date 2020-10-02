def solve(matrix):
    knights_removed = 0
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == "K":
                knights_removed += attack_spots((i, j), matrix)
    print(knights_removed)


def attack_spots(loc, matrix):
    size = len(matrix)
    knights_removed = 0
    x, y = loc
    attack_spots = []

    for coef_1 in [-1, +1]:
        for coef_2 in [-2, +2]:
            attack_spots.append((coef_1, coef_2))

    for coef_1 in [-2, +2]:
        for coef_2 in [-1, +1]:
            attack_spots.append((coef_1, coef_2))

    for attack_spot in attack_spots:
        coef_1, coef_2 = attack_spot
        if 0 <= x + coef_1 < size and 0 <= y + coef_2 < size:
            if matrix[x + coef_1][y + coef_2] == "K":
                matrix[x + coef_1][y + coef_2] = "0"
                knights_removed += 1
    
    return knights_removed


matrix = []

size = int(input())

for _ in range(size):
    matrix.append(list(input()))

solve(matrix)