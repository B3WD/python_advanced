num_rows = int(input())

matrix = [input().split(", ") for _ in range(num_rows)]

first_diag = [matrix[i][i] for i in range(len(matrix))]
second_diag = [matrix[i][-(i + 1)] for i in range(len(matrix))]

print(f"First diagonal: {', '.join(first_diag)}. Sum: {sum(map(int, first_diag))}")
print(f"Second diagonal: {', '.join(second_diag)}. Sum: {sum(map(int, second_diag))}")