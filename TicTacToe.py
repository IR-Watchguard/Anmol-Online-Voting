import os


def display(grid):
    '''Displays The Tic Tac Toe Grid'''
    os.system('cls')  # Clears the terminal everytime the function is called
    for row in grid:
        print(f'{row}\n')


def player_choice():
    '''Takes the first player input'''
    choice = ''
    while choice not in ['X', 'O']:
        # upper() used because the user can input lower case letters
        choice = input('Player 1, Choose X or O : ').upper()

    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def put_marker(grid, row, col, marker):
    '''Places the marker on the desired position'''
    grid[row-1][col-1] = marker


def win_check(grid):
    '''Checks the winning conditions'''
    if grid[0][0] == grid[0][1] == grid[0][2] != ' ':
        return grid[0][0]
    if grid[1][0] == grid[1][1] == grid[1][2] != ' ':
        return grid[1][0]
    if grid[2][0] == grid[2][1] == grid[2][2] != ' ':
        return grid[2][0]
    if grid[0][0] == grid[1][0] == grid[2][0] != ' ':
        return grid[0][0]
    if grid[0][1] == grid[1][1] == grid[2][1] != ' ':
        return grid[0][1]
    if grid[0][2] == grid[1][2] == grid[2][2] != ' ':
        return grid[0][2]
    if grid[0][0] == grid[1][1] == grid[2][2] != ' ':
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != ' ':
        return grid[0][2]
    else:
        return ' '


def check_space(grid, row, col):
    if row in [1, 2, 3] and col in [1, 2, 3]:
        return grid[row-1][col-1] == ' '
    else:
        False


def check_grid_full(grid):
    '''Checks if the grid is all marked or not'''
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == ' ':
                return False

    return True


def player_turn(grid):
    '''Takes input of row and column where the user want to place its marker'''
    row = -1
    col = -1

    while True:
        row = int(input('Please Select The Row From (1,2 or 3) : '))
        col = int(input('Please Select The Column From (1,2 or 3) : '))
        if row in [1, 2, 3] and col in [1, 2, 3] and check_space(grid, row, col):
            return (row, col)


print('WELCOME TO TIC TAC TOE')
while True:
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    p1_mark, p2_mark = player_choice()
    turn = 1
    play_game = True
    # turn_count = 0
    while play_game:
        if check_grid_full(grid):
            print('GAME DRAW!!')
            play_game = False
            break
        if turn == 1:
            display(grid)
            row, col = player_turn(grid)
            put_marker(grid, row, col, p1_mark)
            turn = 2
        else:
            display(grid)
            row, col = player_turn(grid)
            put_marker(grid, row, col, p2_mark)
            turn = 1

        marker = win_check(grid)
        if marker != ' ':
            if marker == p1_mark:
                print(f'PLAYER 1 WON!!')
                break
            else:
                print(f'PLAYER 2 WON!!')
                break
