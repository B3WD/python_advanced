def swap(coords, matrix):
    x_1, y_1, x_2, y_2 = map(int, coords)
    if 0 <= x_1 < rows_count and 0 <= y_1 < cols_count and 0 <= x_2 < rows_count and 0 <= y_2 < cols_count:
        matrix[x_1][y_1], matrix[x_2][y_2] = matrix[x_2][y_2], matrix[x_1][y_1]
        [print(" ".join(map(str, x))) for x in matrix]
    else:
        print("Invalid input!")


matrix = []

rows_count, cols_count = map(int, input().split())

for _ in range(rows_count):
    matrix.append([x for x in input().split()])


while True:
    command = input()
    command = command.split()
    if "END" in command:
        break
    elif "swap" in command and len(command) == 5:
        coords = command[1:]
        swap(coords, matrix)
    else:
        print("Invalid input!")