def solve(matrix):
    knights_removed = 0
    current_best_knight = (0, (0, 0))
    size = len(matrix)
    while True:
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == "K":
                    current_knight = find_best_attacker((i, j), matrix)
                    if current_knight[0] > current_best_knight[0]:
                        current_best_knight = current_knight
        if current_best_knight[0] == 0:
            print(knights_removed)
            break
        best_knight_x, best_knight_y = current_best_knight[1]
        matrix[best_knight_x][best_knight_y] = "0"
        current_best_knight = (0, (0, 0))
        knights_removed += 1


def find_best_attacker(loc, matrix):
    """
    Find the knight that can hit the most figs. Return how many it can hit and pos.
    """
    size = len(matrix)
    knights_to_remove = 0
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
                knights_to_remove += 1
    
    return (knights_to_remove, loc)


matrix = []

size = int(input())

for _ in range(size):
    matrix.append(list(input()))

solve(matrix)