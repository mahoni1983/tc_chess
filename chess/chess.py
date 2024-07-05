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
white_figure_place = None
white_figure = None

def generate_places():
    global places_and_figures
    for y in range(1, board_size + 1):
        for x in range(1, board_size + 1):
            places_and_figures[(x, y)] = ''


def show_info():
    print("""It is a program which will answer a simple question – \
    given a board state that the user enters, with 1 white figure and up to 16 black figures, which black figures can \
    the white figure take?""")


def get_figure_and_place_from_input(text: str):
    figure, place_letter_number = text.strip().lower().split()
    if figure not in figures_names:
        print(f'{figure} is not as expected. Possible figures: {figures_names}')
        raise ValueError
    place = get_xy_coordinates_from_letter_number(place_letter_number)
    if place not in places_and_figures:
        print('The place is outside of the board. A place must be from a1 to h8')
        raise ValueError
    return figure, place


def prompt_to_input_white_figure():
    global white_figure_place
    global white_figure
    while not white_figure_place:
        text = input(f'Please input white figure and its place (from a1 to h8), e.g. knight a5, possible figures: '
                     f'{figures_names}:\n')
        try:
            figure, place = get_figure_and_place_from_input(text)
            places_and_figures[place] = f'white {figure}'
            white_figure_place = place
            white_figure = figure
        except ValueError:
            print('Wrong input.')


def prompt_to_input_figures():
    print(f'Please input black figures and their places (from a1 to h8) one by one. Up to {figures_count_limit} pcs.\n'
                 f'Possible figures: {figures_names}.')
    figure_number = 1
    while True:
        if figure_number == 1:
            text = input(f'Please input figure {figure_number} and it\'s place (e.g. knight a5): ')
        elif figure_number <= figures_count_limit:
            text = input(f'Please input figure {figure_number} and it\'s place (e.g. knight a5) or "done" '
                         f'(without quotes) to finish input: ')
        else:
            print('Figure number limit achieved. No more figures can be added.')
            break

        if figure_number > 1 and text.lower() == 'done':
            break

        try:
            figure, place = get_figure_and_place_from_input(text)
            if places_and_figures[place] == '':
                places_and_figures[place] = figure
                figure_number += 1
            else:
                print(f'The place is already occupied. Please choose another place.')
                continue
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


def get_threats_list(threat_to):
    threats = []
    places_occupied = [{place: figure} for place, figure in places_and_figures.items() if figure in figures_names]
    for place in places_occupied:

        threat = is_threat_from_figure(place, threat_to=threat_to)
        if threat:
            if threat_to == 'white':
                threats.append(place)
            elif threat_to == 'black':
                threats.append(place)
    return threats


def is_threat_from_figure(place_with_figure, threat_to):
    """
    defines whether there is a threat from specified figure to the other specified side (white or black).
    If threat_to is 'white': a threat is defined to the white figure from black figures.
    If threat_to is 'black': a threat is defined to black figures from the white figure.
    :param place_with_figure: place and figure to define threat from
    :param threat_to: 'white' or 'black'. Whom to define a threat to.
    :return: True or False when threat_to is white. place or None when threat_to is black
    """
    x, y = list(place_with_figure.keys())[0]
    if threat_to == 'white':
        figure = place_with_figure[(x, y)]
    elif threat_to == 'black':
        figure = white_figure
        # x, y = white_figure_place
    moves = figures[figure]['moves']
    long_step = figures[figure]['long_step']
    for move in moves:
        x_move, y_move = move
        place_moved_to = (x + x_move, y + y_move)
        while True:
            if place_moved_to in places_and_figures:
                place_moved_to_occupied_by = places_and_figures[place_moved_to]
                if threat_to == 'white':
                    if place_moved_to_occupied_by.startswith('white'):
                        # it is a threat
                        return True
                    elif place_moved_to_occupied_by != '':
                        # another black figure is on the way
                        break
                elif threat_to == 'black':
                    if place_moved_to == white_figure_place:
                        # black figure is on the way. the white figure makes a threat to it
                        return True

                # if place_moved_to_occupied_by == '':    -  not occupied place
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
    prompt_to_input_white_figure()
    prompt_to_input_figures()
    places_occupied = [{place: figure} for place, figure in places_and_figures.items() if figure in figures_names]
    print(f'List of all inputted figures: {places_occupied}')
    threats_to_white = get_threats_list('white')
    if threats_to_white:
        print(f'{len(threats_to_white)} threat/s to the white figure detected from figure/s: {threats_to_white}')
    else:
        print('No threats detected to the white figure.')

    threats_to_black = get_threats_list('black')
    if threats_to_black:
        print(f'{len(threats_to_black)} threat/s to black figures detected from the white figure: {threats_to_black}')
    else:
        print('No threats detected from the white figure.')


start_program()
