matrix = []

for _ in range(int(input())):
    matrix.append([int(x) for x in input().split()])

def first_diag_sum(matrix):
    diag_sum = 0
    for i, _ in enumerate(matrix):
        diag_sum += matrix[i][i]
    return diag_sum


def second_diag_sum(matrix):
    diag_sum = 0
    columns_count = len(matrix)
    for i, _ in enumerate(matrix):
        diag_sum += matrix[i][columns_count - 1 - i]
    return diag_sum


print(abs(first_diag_sum(matrix) - second_diag_sum(matrix)))