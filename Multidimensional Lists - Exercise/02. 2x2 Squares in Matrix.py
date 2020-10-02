def find_2x2_matching(matrix):
    matches = 0
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
                matches += 1
    print(matches)


matrix = []

rows_count, cols_count = map(int, input().split())

for _ in range(rows_count):
    matrix.append([x for x in input().split()])

find_2x2_matching(matrix)
