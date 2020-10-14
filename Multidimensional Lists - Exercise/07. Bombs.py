def solve_bombs(matrix, bombs):
    for bomb in bombs:
        x, y = map(int, bomb.split(","))
        damage_cells_around(x, y)

    alive_count, suma = find_alive_cells(matrix)
    print(f"Alive cells: {alive_count}")
    print(f"Sum: {suma}")
    [print(" ".join(map(str, x))) for x in matrix]


def find_alive_cells(matrix):
    alive_count = 0
    suma = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] > 0:
                alive_count += 1
                suma += matrix[i][j]

    return alive_count, suma



def damage_cells_around(x, y):
    value = matrix[x][y]

    if value <= 0:
        return None

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= j < size and 0 <= i < size and matrix[i][j] > 0:
                matrix[i][j] -= value


matrix = []

size = int(input())

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

solve_bombs(matrix, bombs)