def play_war_planes(field, commands):
    plane_loc = locate_pieces("p", field)[0]
    targets_locs = locate_pieces("t", field)
    init_target_count = len(targets_locs)

    for command in commands:
        
        if not targets_locs:
            break

        if "shoot" in command:
           direction, steps = command[1], int(command[2])
           shoot_at_target(plane_loc, direction, steps, targets_locs, field)

        elif "move" in command:
            direction, steps = command[1], int(command[2])
            plane_loc = move_plane(plane_loc, direction, steps, field)

    if targets_locs:
        print(f"Mission failed! {len(targets_locs)} targets left.")
    else:
        print(f"Mission accomplished! All {init_target_count} targets destroyed.")

    print_field(field)


def print_field(field):
    [print(*row) for row in field]


def read_commands(commands_count):
    return [input().split() for _ in range(commands_count)]


def locate_pieces(piece, field):
    coords = []
    for (i, row) in enumerate(field):
        for (j, col) in enumerate(row):
            if field[i][j] == piece:
                coords.append([i, j])
    return coords


def shoot_at_target(plane_coords, direction, steps, targets_locs, field):
    (i, j) = plane_coords
    if direction == "left":
        coords_of_hit = [i, j - steps]
    elif direction == "right":
        coords_of_hit = [i, j + steps]
    elif direction == "up":
        coords_of_hit = [i - steps, j]
    elif direction == "down":
        coords_of_hit = [i + steps, j]

    if valid_pos(coords_of_hit, field, mode="shoot"):
        execute_shot(coords_of_hit, targets_locs, field)


def execute_shot(coords_of_hit, targets_locs, field):
    (i, j) = coords_of_hit
    for targets_loc in targets_locs:
        if targets_loc == coords_of_hit:
            targets_locs.remove([i, j])
    field[i][j] = "x"


def move_plane(plane_coords, direction, steps, field):
    (i, j) = plane_coords
    if direction == "left":
        new_coords = (i, j - steps)
    elif direction == "right":
        new_coords = (i, j + steps)
    elif direction == "up":
        new_coords = (i - steps, j)
    elif direction == "down":
        new_coords = (i + steps, j)

    if valid_pos(new_coords, field, mode="move"):
        (new_i,new_j) = new_coords
        field[i][j] = "."
        field[new_i][new_j] = "p"
        return new_coords
    else:
        return plane_coords

    
def valid_pos(coords, field, mode = None):
    flag = True
    (i, j) = coords
    size = len(field)
    
    if 0 <= i < size and 0 <= j < size:
        if mode == "move":
            if field[i][j] != ".":
                flag = False
        elif mode == "shoot":
            if field[i][j] in {"x", "p"}:
                flag = False
    else:
        flag = False
   
    return flag


rows_count = int(input())
field = [input().split() for _ in range(rows_count)]
commands_count = int(input())
commands = read_commands(commands_count)
play_war_planes(field, commands)