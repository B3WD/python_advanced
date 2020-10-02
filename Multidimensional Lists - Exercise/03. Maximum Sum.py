def find_biggest_sum(matrix):
    loc = 0, 0
    biggest_sum = 0
    current_sum = 0
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[i]) - 2):
            current_sum = sum_3x3((i, j), matrix)
            if current_sum > biggest_sum:
                loc = (i, j)
                biggest_sum = current_sum
    print(f"Sum = {biggest_sum}")
    print_3x3(loc, matrix)


def sum_3x3(loc : tuple, matrix):
    start_row, start_column = loc
    sum_ = 0
    for i in range(3):
        for j in range(3):
            sum_ += matrix[start_row + i][start_column + j]
    return sum_


def print_3x3(loc, matrix):
    matrix_3x3 = []
    start_row, start_column = loc
    for i in range(3):
        matrix_3x3.append(matrix[start_row + i][start_column : start_column + 3])
    [print(" ".join(map(str, x))) for x in matrix_3x3]


matrix = []

rows_count, cols_count = map(int, input().split())

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split()])

find_biggest_sum(matrix)