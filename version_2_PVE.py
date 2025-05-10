def minmax(board,is_maximizing):
    winner=check_winner(board)
    if winner=="X": return -1
    if winner=="O": return 1
    if winner=="Draw": return 0

    if is_maximizing: