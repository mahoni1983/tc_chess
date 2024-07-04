"""For this task, you are asked to create a console based tic-tac-toe game in which the computer will play against
you. The good news is that you will be able to win sometimes, as the computer will play randomly! You are provided
with these requirements for the program:

The user always makes the first move The user should be asked to input their move until the game ends. The format for
input should be “x, y” where x is the horizontal axis and y is the vertical axis. Upper left spot is 0, 0,
lower right is 2, 2. (While it can seem weird at first, developers love indexing things from 0). You can assume that
the user will always enter their input in the form “,” (i.e., no negative numbers, letters, symbols and
multiple-digit numbers) After the user enters a move, the computer should make their move, if possible. Every time
the computer makes its move, the state of the board should be printed out. The design does not need to be perfect –
the important thing is that the state of the board should be clear. If either the player or the computer wins,
the state of the board should be printed out and the winner announced. The program should exit at that point.
Additional challenge: if you are more proficient at coding and find the task relatively easy (e.g. it took you less
than four hours to complete), try to make the computer play optimally instead of randomly. Be sure to still read the
suggested solution document, though! """

import random

board_size = 3
user_character = 'x'
pc_character = 'o'
users_turn_to_play = True
is_game_over = False
free_cells = []
turns_user = []
turns_pc = []
winner = ''


def ask_user_for_board_size():
    board_size_proposal = 0
    while not board_size_proposal:
        text = input(f'Please choose the board length. One integer: 3 or greater.')
        try:
            board_size_proposal_try = int(text)
            if board_size_proposal_try >=3:
                board_size_proposal = board_size_proposal_try
        except:
            print('Integer only can accepted.')
    global board_size
    board_size = board_size_proposal



def define_free_cells():
    global free_cells
    free_cells = [(x, y) for x in range(board_size) for y in range(board_size)]


def switch_turn():
    global users_turn_to_play
    users_turn_to_play = True if not users_turn_to_play else False


def make_users_turn():
    while True:
        cell_chosen = prompt_user_to_play()
        if can_cell_be_chosen(cell_chosen):
            turns_user.append(cell_chosen)
            free_cells.remove(cell_chosen)
            switch_turn()
            break


def is_player_a_winner(turns_player):
    horizontal_win = []
    vertical_win = []
    win_check_list = []
    # diagonal win
    win_check_list.append(all([(i, i) in turns_player for i in range(board_size)]))
    # another diagonal win
    win_check_list.append(all([(board_size-1-i, i) in turns_player for i in range(board_size)]))
    for i in range(board_size):
        win_check_list.append(all([(x, i) in turns_player for x in range(board_size)]))
        win_check_list.append(all([(i, y) in turns_player for y in range(board_size)]))
    return any(win_check_list)


def start_game():
    print("Let's start the game.")
    define_free_cells()
    draw_board()

    play_game()
    print('Gave over')


def play_game():
    # define_free_cells()
    # draw_board()
    global users_turn_to_play
    while free_cells:
        if users_turn_to_play:
            make_users_turn()
            if is_player_a_winner(turns_user):
                draw_board()
                print(f'Congratulations! YOU WON!!')
                break
        else:
            prompt_pc_to_play()
            if is_player_a_winner(turns_pc):
                draw_board()
                print(f'Game over. PC won.')
                break
        draw_board()


def can_cell_be_chosen(cell_chosen):
    x,y = cell_chosen
    if x < 0 or y < 0:
        print('Chosen cell is outside of the board')
        return False
    if x > board_size-1 or y > board_size -1:
        print('Chosen cell is outside of the board')
        return False
    if cell_chosen not in free_cells:
        print(f'The chosen cell is already occupied.')
        return False
    return True


def prompt_user_to_play():
    while True:
        try:
            text = input('Make turn: x,y\n')
            x, y = text.split(',')
            x, y = int(x), int(y)
            return x, y
        except ValueError:
            print('Wrong input. Two integers are expected, divided by comma. x,y')
        except Exception as e:
            # print('Wrong input. Two integers are expected, divided by comma. x,y')
            print(f'Stopping the program due to error:\n{e}')
            break


def prompt_pc_to_play():
    print('prompt_pc_to_play')
    cell_chosen = random.choice(free_cells)

    # double check
    if can_cell_be_chosen(cell_chosen):
        print(f'PC chose: {cell_chosen}')
        turns_pc.append(cell_chosen)
        free_cells.remove(cell_chosen)
        switch_turn()
    pass


def draw_board():
    vertical_border = '|'
    cell_filler = '   '
    even_row = ''
    odd_row = ''
    horizontal_border = '---'
    node = '+'
    board = []

    user_turns_on_board = transform_turns(turns_user)
    pc_turns_on_board = transform_turns(turns_pc)

    for _ in range(board_size-1):
        even_row += cell_filler + vertical_border
        odd_row += horizontal_border + node
    even_row += cell_filler
    odd_row += horizontal_border

    # draw board
    for i in range(board_size*2 - 1):
        # board.append(even_row if i%2 == 0 else odd_row)
        if i%2 == 0:
            cur_row = even_row
            for x, y in user_turns_on_board:
                if y == i:
                    cur_row = cur_row[:x] + user_character + cur_row[x+1:]
            for x, y in pc_turns_on_board:
                if y == i:
                    cur_row = cur_row[:x] + pc_character + cur_row[x+1:]
            board.append(cur_row)
        else:
            board.append(odd_row)
    for row in board:
        print(row)


def transform_turns(turns):
    """ defines coordinates on board by given 'human' coordinates"""
    turns_transformed = []
    for turn in turns:
        x, y = turn
        turns_transformed.append((x*4 + 1, y*2))
    return turns_transformed

print('It is tic-tac-toe game. ')
ask_user_for_board_size()
start_game()

"""
012345678910
   |   |    0
---+---+--- 1
   |   |    2
---+---+--- 3
   |   |    4
   
012345678910
 x |   |    0
---+---+--- 1
   | x |    2
---+---+--- 3
   |   | x  4


"""
