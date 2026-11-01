while True:
    try:
        board = [list(map(int, input().split())) for _ in range(3)]
        lines = [
            board[0], board[1], board[2],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]
        ]
        has_winner = any(len(set(line)) == 1 for line in lines)
        print(has_winner)
    except EOFError:
        break
