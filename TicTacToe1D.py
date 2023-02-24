import os


def display(grid):
    '''Displays The Tic Tac Toe Grid'''
    os.system('cls')  # Clears the terminal everytime the function is called
    print(f'"{grid[0]}" "{grid[1]}" "{grid[2]}"')
    print(f'"{grid[3]}" "{grid[4]}" "{grid[5]}"')
    print(f'"{grid[6]}" "{grid[7]}" "{grid[8]}"')


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


def put_marker(grid, position, marker):
    '''Places the marker on the desired position'''
    grid[position] = marker


def win_check(grid, marker):
    '''Checks the winning conditions'''
    return (
        (grid[6] == marker and grid[7] == marker and grid[8] == marker) or
        (grid[3] == marker and grid[4] == marker and grid[5] == marker) or
        (grid[0] == marker and grid[1] == marker and grid[2] == marker) or
        (grid[6] == marker and grid[3] == marker and grid[0] == marker) or
        (grid[7] == marker and grid[4] == marker and grid[1] == marker) or
        (grid[8] == marker and grid[5] == marker and grid[2] == marker) or
        (grid[6] == marker and grid[4] == marker and grid[2] == marker) or
        (grid[8] == marker and grid[4] == marker and grid[0] == marker))


def check_space(grid, position):
    if position in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return grid[position-1] == ' '
    else:
        False


def check_grid_full(grid):
    '''Checks if the grid is all marked or not'''
    for i in range(0, len(grid)):
        if grid[i] == ' ':
            return False

    return True


def player_turn(grid):
    '''Takes input of row and column where the user want to place its marker'''
    position = -1

    while True:
        position = int(input('Please Select The Row From [1-9] : '))
        if position in range(1, 10) and check_space(grid, position):
            return position-1


print('WELCOME TO TIC TAC TOE')
while True:
    grid = [' '] * 9
    p1_mark, p2_mark = player_choice()
    turn = 1
    play_game = True
    while play_game:
        if turn == 1:
            display(grid)
            position = player_turn(grid)
            put_marker(grid, position, p1_mark)
            if win_check(grid, p1_mark):
                display(grid)
                print('CONGRATULATIONS PLAYER 1 WON!!')
                play_game = False
            else:
                if check_grid_full(grid):
                    print('GAME DRAW!!')
                    play_game = False
                else:
                    turn = 2
        else:
            display(grid)
            position = player_turn(grid)
            put_marker(grid, position, p2_mark)
            if win_check(grid, p2_mark):
                display(grid)
                print('CONGRATULATIONS PLAYER 2 WON!!')
                play_game = False
            else:
                if check_grid_full(grid):
                    print('GAME DRAW!!')
                    play_game = False
                else:
                    turn = 1
