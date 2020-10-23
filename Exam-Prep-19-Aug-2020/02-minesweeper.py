def generate_minfield(field, bomb_locs):
    place_bombs(field, bomb_locs)
    for i, row in enumerate(field):
        for j, col in enumerate(row):
            if field[i][j] != "*":
                hits = check_3x3([i, j], field)
                field[i][j] = hits
    
    [print(*row) for row in field]


def check_3x3(pos, field):
    N = 2
    (i, j) = pos
    hits = 0

    for x in {-1, 0, 1}:
        for y in {-1, 0, 1}:
            if valid_pos([i + x, j + y], len(field)):
                if field[i + x][j + y] == "*":
                    hits += 1

    return hits


def valid_pos(pos, size):
    flag = False
    (i, j) = pos
    if 0 <= i < size and 0 <= j < size:
        flag = True

    return flag


def get_bomb_locs(count):
    bomb_locs = []
    for _  in range(count):
        bomb = input().split(", ")
        (i, j) = int(bomb[0][1:]), int(bomb[1][:-1])
        bomb_locs.append([i, j])

    return bomb_locs


def place_bombs(field, bomb_locs):
    for bomb in bomb_locs:
        if valid_pos(bomb, len(field)):
            (i, j) = bomb
            field[i][j] = "*"


size = int(input())
bombs_count = int(input()) 

field = [[0] * size for _ in range(size)]
bomb_locs = get_bomb_locs(bombs_count)

generate_minfield(field, bomb_locs)