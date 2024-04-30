

def create_board(fill): 
    """Create 8x8 board and fill it with `fill` value."""
    return [
        [fill for _ in range(8)]
        for _ in range(8)
    ]


def usr2coord(position: str): 
    """Transform position c2 to (2, 1)."""

    alphabet = 'abcdefgh'
    x, y = position
    assert x in alphabet, y in '12345678'
    return alphabet.index(x), int(y) - 1


def coord2usr(position: tuple): 
    """Transform position (2, 1) to c2."""
    alphabet = 'abcdefgh'
    x, y = position
    return f'{alphabet[x]}{y + 1}'


def knight_moves(start_pos: tuple): 
    """Return every possible cells where knight can move."""
    x, y = start_pos

    res_pos = []
    for delta_x, delta_y in [[1, 2], [1, -2], [-1, 2], [-1, -2], 
                             [2, 1], [2, -1], [-2, 1], [-2, -1]]:
        next_x, next_y = x + delta_x, y + delta_y
        if 0 <= next_x < 8 and 0 <= next_y < 8: 
            res_pos.append((next_x, next_y))
    return res_pos


def knight_reach(start_pos: tuple): 
    """BFS around every cell and find minimal amount of 
    moves a knight needs to make from the start_pos to reach 
    this cell.
    
    :param start_pos: (x, y) coordinate 
    :return: 
        board: 
            8x8 array with entities that is minimal amount of moves to make 
            from the start_pos 
        
        board_from: 
            8x8 array with entities that is coordinates of the previous cell 
            in the shortest path from the start_pos
    """
    start_x, start_y = start_pos
    board = create_board(-1)
    board_from = create_board(None)

    board[start_x][start_y] = 0

    # queue with cells, which we can reach on the next move
    queue = [(next_pos, 1, start_pos) for next_pos in knight_moves(start_pos)]
    
    # while queue is not empty 
    while queue: 

        (cur_x, cur_y), moves_amount, from_pos = queue.pop(0)
        
        # if we've reached this cell already, skip it 
        if board[cur_x][cur_y] != -1: 
            continue 

        # save the minimal amount of moves and from which cell we came 
        board[cur_x][cur_y] = moves_amount
        board_from[cur_x][cur_y] = from_pos

        # expand the queue with cells we can reach from the current position
        queue += [
            (next_pos, moves_amount + 1, (cur_x, cur_y)) 
            for next_pos in knight_moves((cur_x, cur_y))
        ]
    return board, board_from


def knight_min_moves(start_pos, end_pos): 
    x, y = end_pos
    board, board_from = knight_reach(start_pos)
    return board[x][y], rebuild_path(board_from, end_pos)


def rebuild_path(board_from, end_pos): 
    """Recreate the full path from start_pos to the end_pos, having 
    the board_from, that is the output of `knight_reach` function."""
    path = []
    cur_pos = end_pos
    while cur_pos is not None: 
        path.append(cur_pos)
        x, y = cur_pos
        cur_pos = board_from[x][y]
    return path[::-1]


if __name__ == "__main__": 

    for i in range(8): 
        for j in range(8): 
            assert usr2coord(coord2usr((i, j))) == (i, j) 

    assert coord2usr((0, 0)) == 'a1'


    test_board, test_board_from = knight_reach((0, 0))
    for row in test_board: 
        print(*row)

    print()
    for row in test_board_from: 
        print(*row)

    start_pos = input("Enter the start position:\n--> ")
    end_pos = input("Enter the end position:\n--> ")
    start_pos = usr2coord(start_pos)
    end_pos = usr2coord(end_pos)

    res, path = knight_min_moves(start_pos, end_pos)
    print(res)
    print(' -> '.join(coord2usr(el) for el in path))
