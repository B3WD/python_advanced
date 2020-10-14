def store_lines_until_command(stop_command):
    while True:
        command = input().split()
        if stop_command in command:
            break
        else:
            action, m, n, num = command[0], int(command[1]), int(command[2]), int(command[3])
            solve(matrix, action, n, m, num)

def solve(matrix, action, m, n, num):
    if not (0 <= m < rows_count and 0 <= n < rows_count):
        print("Invalid coordinates")
    elif action == "Add":
        matrix[m][n] += num
    elif action == "Subtract":
        matrix[m][n] -= num

rows_count = int(input())

matrix = [list(map(int, input().split())) for _ in range(rows_count)]

store_lines_until_command("END")

[print(" ".join(map(str ,row))) for row in matrix]