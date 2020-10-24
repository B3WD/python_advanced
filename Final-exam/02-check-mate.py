def play_chess(board):
    winner_queens = []

    queen_locs = get_piece_pos("Q", board)
    king_loc = get_piece_pos("K", board)

    for queen_loc in queen_locs:
        if queen_wins(queen_loc, board):
            winner_queens.append(queen_loc)

    if winner_queens:
        [print(x) for x in winner_queens]
    else:
        print("The king is safe!")


def get_piece_pos(piece, board):
    locs = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] == piece:
                locs.append([i, j])

    return locs


def queen_wins(piece, board):
    (i, j) = piece

    hits_king = False

    for x in {-1, 0, 1}:
        dir_x = x
        for y in {-1, 0, 1}:

            while True:

                if not valid_loc([i + x, j + y], board):
                    x = dir_x
                    break

                if board[i + x][j + y] == "K":
                    x = dir_x
                    hits_king = True
                    break

                elif board[i + x][j + y] == "Q":
                    x = dir_x
                    break 

                if x < 0:
                    x -= 1

                if x > 0:
                    x += 1

                if y < 0:
                    y -= 1

                if y > 0:
                    y += 1

    return hits_king            


def valid_loc(loc, board):
    validity = False
    (i, j) = loc
    size = len(board)

    if 0 <= i < size and 0 <= j < size:
        validity = True

    return validity


board = [input().split() for _ in range(8)]

play_chess(board)