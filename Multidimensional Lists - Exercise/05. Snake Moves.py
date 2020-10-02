from collections import deque

matrix = []

rows_count, cols_count = map(int, input().split())
snake = deque(input())

for i in range(rows_count):
    word = ""
    for j in range(cols_count):
        current_letter = snake[0]
        word += current_letter
        snake.append(snake.popleft())
    if i % 2 != 0:
        print(word[::-1])
    else:
        print(word)