rows_count = int(input())


def get_snake_pos(matrix):
    for i, row in enumerate(matrix):
        if "S" in row:
            j = row.index("S")
            snake_pos = [i, j]
            return snake_pos


def get_food_pos(matrix):
    food_positions = []
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            if matrix[i][j] == "*":
                food_positions.append([i, j])
    return food_positions


def get_lair(matrix):
    lair_positions = []
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            if matrix[i][j] == "B":
                lair_positions.append([i, j])
    return lair_positions


def move_left(snake_pos):
    (i, j) = snake_pos
    new_snake_pos = [i, j - 1]
    return new_snake_pos


def move_right(snake_pos):
    (i, j) = snake_pos
    new_snake_pos = [i, j + 1]
    return new_snake_pos


def move_up(snake_pos):
    (i, j) = snake_pos
    new_snake_pos = [i - 1, j]
    return new_snake_pos


def move_down(snake_pos):
    (i, j) = snake_pos
    new_snake_pos = [i + 1, j]
    return new_snake_pos


def on_food(snake_pos, food):
    flag = False
    for food_pos in food:
        if snake_pos == food_pos:
            flag = True
    return flag


def on_lair(snake_pos, lairs):
    flag = False
    for lair_pos in lairs:
        if snake_pos == lair_pos:
            flag = True
    return flag


def leave_trail(matrix, snake_pos):
    (i, j) = snake_pos
    matrix[i][j] = "."


def out_of_field(snake_pos, rows_count):
    flag = False
    (i, j) = snake_pos
    if not (0 <= i <= rows_count - 1) or not (0 <= j <= rows_count - 1):
        flag = True
    return flag


field = [input() for _ in range(rows_count)]

# Get initial coords fo pieces
food = get_food_pos(field)
snake_pos = get_snake_pos(field)
lairs = get_lair(field)

food_count = 0

field = [list(row) for row in field]

while True:
    command = input()

    if command == "left":
        leave_trail(field, snake_pos)
        snake_pos = move_left(snake_pos)

    elif command == "right":
        leave_trail(field, snake_pos)
        snake_pos = move_right(snake_pos)

    elif command == "up":
        leave_trail(field, snake_pos)
        snake_pos = move_up(snake_pos)

    elif command == "down":
        leave_trail(field, snake_pos)
        snake_pos = move_down(snake_pos)

    if out_of_field(snake_pos, rows_count):
        print("Game over!")
        break

    elif on_food(snake_pos, food):
        food_count += 1
        food.remove(snake_pos)
        
    elif on_lair(snake_pos, lairs):
        lairs.remove(snake_pos)
        leave_trail(field, snake_pos)
        snake_pos = lairs[0]
        lairs = []

    if food_count >= 10:
        print("You won! You fed the snake.")
        (i, j) = snake_pos
        field[i][j] = "S"
        break

print(f"Food eaten: {food_count}")
[print(''.join(row)) for row in field]