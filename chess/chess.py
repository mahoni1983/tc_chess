"""
The first practical graded task will require you to implement a Python program which will answer a simple question –
given a board state that the user enters, with 1 white figure and up to 16 black figures, which black figures can the
white figure take?

The exact criteria you are given to implement are as follows:
The program should first ask the user to input a chess piece and where it is on the board. This will be the white
piece. The user should be informed that they can choose between two pieces of your choice (e.g. pawn and rook). The
choice should be made by writing the piece and the coordinates in a predefined format in the console, e.g.: knight a5
Once the user successfully adds the white piece, the user is asked to enter the black pieces, one by one, in the same
format as the white piece. They need to add at least 1 black piece or 16 at most. Once at least one black piece has
been added, the user can write “done” instead of the coordinates to add no more pieces. You can assume that the user
will input either “done” or the correct format for adding a piece (“piece coordinates”). You can also assume that
coordinates will always be entered as where letters are a-h and digits are 1-8, e.g. a1, d4, h8. You should not
assume anything else about the inputs, however (hint: there are still at least a couple of ways for the user to make
invalid input, e.g. trying to write “done” too early) After adding each piece, there should be either a confirmation
that it was added successfully, or an error message explaining what the issue is. After the white and the black
pieces are added, the program should print out the black pieces, if any, that the white piece can take. """


"""
King - Moves one square in any direction.
Queen - Moves any number of squares diagonally, horizontally, or vertically.
Rook - Moves any number of squares horizontally or vertically.
Bishop - Moves any number of squares diagonally.
Knight - Moves in an ‘L-shape,’ two squares in a straight direction, and then one square perpendicular to that.
Pawn - Moves one square forward, but on its first move, it can move two squares forward. It captures diagonally one 
square forward."""

board_size = 8
places_and_figures = {}
figures_count_limit = 16
figures_names = {'king', 'queen', 'rook', 'bishop', 'knight', 'pawn'}
figures = {'king': {'long_step': False, 'moves': [(-1, -1), (-1, 0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]},
           'queen': {'long_step': True, 'moves': [(-1, -1), (-1, 0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]},
           'rook': {'long_step': True, 'moves': [(-1, 0), (0, -1), (0, 1), (1, 0)]},
           'bishop': {'long_step': True, 'moves': [(-1, -1), (-1, 1), (1, -1), (1, 1)]},
           'knight': {'long_step': False, 'moves': [(-2, -1), (-2, 1), (2,-1), (2,1), (1,2), (-1,2), (-1,-2), (1,-2)]},
           'pawn': {'long_step': False, 'moves': [(-1, -1), (-1, 1), (1, -1), (1, 1)]}}
target = None


def generate_places():
    global places_and_figures
    for y in range(1, board_size + 1):
        for x in range(1, board_size + 1):
            places_and_figures[(x, y)] = ''


def show_info():
    print("""It is a program which will answer a simple question –
    given a board state that the user enters, with 1 white figure and up to 16 black figures, which black figures can 
    the white figure take?""")


def prompt_to_input_target():
    global target
    while True:
        text = input('Please input target place (from a1 to h8): ')
        try:
            x, y = get_xy_coordinates_from_letter_number(text)
            if (x, y) in places_and_figures:
                places_and_figures[(x, y)] = 'target'
                target = (x, y)
                break
            else:
                print('The place is outside of the board. Please choose a place within the board (limits).')
        except ValueError:
            print('Wrong input.')


def prompt_to_input_figures():
    print(f'Please input figures and their places (from a1 to h8) one by one. Up to {figures_count_limit} pcs.\n'
                 f'Figures: {figures.keys()}')
    figure_number = 1
    while True:
        if figure_number == 1:
            text = input(f'Please input figure {figure_number} and it\'s place (e.g. knight a5): ')
        elif figure_number < figures_count_limit:
            text = input(f'Please input figure {figure_number} and it\'s place (e.g. knight a5) or "done" '
                         f'(without quotes) to finish input: ')
        else:
            print('Figure number limit achieved. No more figures can be added.')
            break

        if figure_number > 1:
            if text.lower() == 'done':
                break

        try:
            figure, place = text.lower().split()
            if figure not in figures.keys():
                raise ValueError
            x, y = get_xy_coordinates_from_letter_number(place)
            if (x, y) in places_and_figures:
                if places_and_figures[(x, y)] == '':
                    places_and_figures[(x, y)] = figure
                    figure_number += 1
                else:
                    print(f'The place is already occupied. Please choose another place.')
                    continue
                # break
            else:
                print('Please choose a place within the board.')
        except ValueError:
            print('Wrong input.')


def get_xy_coordinates_from_letter_number(letter_number: str):
    letter = letter_number[:1]
    number = letter_number[1:]
    if letter.isalpha() and number.isdigit():
        x = ord(letter.lower()) - 96
        return x, int(number)
    else:
        raise ValueError


def get_threads_list():
    threads = []
    places_occupied = [{place: figure} for place, figure in places_and_figures.items() if figure in figures.keys()]
    for place in places_occupied:
        if is_thread_from_figure(place):
            threads.append(place)
    return threads


def is_thread_from_figure(place_with_figure):
    x, y = list(place_with_figure.keys())[0]
    figure = place_with_figure[(x, y)]
    moves = figures[figure]['moves']
    long_step = figures[figure]['long_step']
    for move in moves:
        x_move, y_move = move
        place_moved_to = (x + x_move, y + y_move)
        while True:
            if place_moved_to in places_and_figures:
                place_moved_to_occupied_by = places_and_figures[place_moved_to]
                if place_moved_to_occupied_by == 'target':
                    # it is a thread
                    return True
                elif place_moved_to_occupied_by != '':
                    # another figure is on the way
                    return False
                elif place_moved_to_occupied_by == '':
                    # free place
                    pass
            else:
                # place is outside of the board
                break

            if long_step:
                # go to next place if the figure can go for long distances
                place_moved_to = (place_moved_to[0] + x_move, place_moved_to[1] + y_move)
            else:
                break


def start_program():
    generate_places()
    show_info()
    prompt_to_input_target()
    prompt_to_input_figures()
    threads = get_threads_list()
    if threads:
        threads_figures_list = [fig for t in threads for fig in t.values()]
        print(f'{len(threads)} thread/s detected from figure/s: {threads_figures_list}')
    else:
        print('No threads detected')


start_program()
