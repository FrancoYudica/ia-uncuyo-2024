def get_neighbors(row, column):
    """Returns the neighbors. Row, column and block"""
    neighbors = set()

    # Adds the same row and column neighbors
    for i in range(9):
        neighbors.add((row, i))
        neighbors.add((i, column))

    # Adds the block neighbors
    block_row_start_index = (row // 3) * 3
    block_column_start_index = (column // 3) * 3

    for i in range(3):
        for j in range(3):
            neighbors.add((block_row_start_index + i, block_column_start_index + j))

    # Removes the (row, column)
    neighbors.discard((row, column))
    return neighbors


def revise(
        domains, 
        xi: tuple, 
        xj: tuple) -> bool:

    xi_domain = domains[xi[0]][xi[1]]
    xj_domain = domains[xj[0]][xj[1]]

    # xj_domain should have one element, since it's already explored
    if len(xj_domain) != 1:
        return False

    xj_value = xj_domain[0]

    if xj_value in xi_domain:
        xi_domain.remove(xj_value)
        return True
    
    return False


def print_sudoku_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Line to separate boxes

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Separator between 3x3 boxes

            if j == 8:
                print(board[i][j] if board[i][j] != 0 else "?")  # End of row, print and move to next line
            else:
                print(board[i][j] if board[i][j] != 0 else "?", end=" ")


def generate_initial_domains(board) -> list:
    """Given the initial board setup, calculates the domain of all the cells"""
    domains = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(9)] for _ in range(9)]

    # The domain of a cell that is already set is it's value
    for row in range(0, 9):
        for column in range(0, 9):
            if board[row][column] != 0:
                domains[row][column] = [board[row][column]]

    return domains


def ac3_sudoku(domains):

    # Initializes queue with all the neighbors of all the cells
    queue = []
    for row in range(0, 9):
        for column in range(0, 9):
            for neighbor in get_neighbors(row, column):
                queue.append(((row, column), neighbor))

    while queue:
        xi, xj = queue.pop(0)

        if revise(domains, xi, xj):

            # If the domain is empty, there isn't solution
            if len(domains[xi[0]][xi[1]]) == 0:
                return False

            # Adds all the neighbors of xi to the queue
            for neighbor in get_neighbors(xi[0], xi[1]):

                # Except for xj
                if neighbor != xj:
                    queue.append((neighbor, xi))
    return True



if __name__ == "__main__":

    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print_sudoku_board(sudoku_board)

    domains = generate_initial_domains(sudoku_board)

    if ac3_sudoku(domains):
        print("Solution found!")
        final_board = [[domains[row][column][0] for column in range(9)] for row in range(9)]
        print_sudoku_board(final_board)
    else:
        print("No solution possible...")