FIRST_LETTER = 97

rows_count, cols_count = map(int, input().split())

matrix = []

for i in range(rows_count):
    row = []
    for j in range(cols_count):
        row.append(chr(FIRST_LETTER + i) + chr(FIRST_LETTER + i + j) + chr(FIRST_LETTER + i))
    matrix.append(row)

[print(" ".join(row))for row in matrix]