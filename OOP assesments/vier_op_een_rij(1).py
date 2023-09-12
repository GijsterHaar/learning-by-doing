import typing


class Player:
    def __init__(self, color) -> None:
        self.color = color

    def __str__(self) -> str:
        return self.color


class Board:
    def __init__(self, width: int, height: int) -> None:
        self._board: list[list[None | Player]] = []
        self._width = width
        self._height = height
        for _ in range(self._height):
            self._board.append([None] * self._width)

    """
        width = height = 4
        
        top left = (y=0, x=3)
        self._board = [
            [0, ☐, ☐, ☐], # y = 0
            [☐, 1, ☐, ☐], # y = 1
            [☐, ☐, 2, ☐], # y = 2
            [☐, ☐, ☐, 3], # y = 3
        ]
        value_of_y2_x1 = self._board[2][1] -> [☐, ☐, 2, ☐]
        """
    def _get_value_with_vertical_offset(self, x: int, y: int, offset: int) -> Player | None:
        if 0 <= y + offset < self._height:
            return self._board[y + offset][x]

    def _get_value_with_horizontal_offset(self, x: int, y: int, offset: int) -> Player | None:
        if 0 <= x + offset < self._width:
            return self._board[y][x + offset]

    def _get_value_with_diagonal_bottom_left_to_top_right_offset(self, x: int, y: int, offset: int) -> Player | None:
        if 0 <= x + offset < self._width and 0 <= y - offset < self._height:
            return self._board[y - offset][x + offset]

    def _get_value_with_diagonal_top_left_to_bottom_right_offset(self, x: int, y: int, offset: int) -> Player | None:
        if 0 <= x + offset < self._width and 0 <= y + offset < self._height:
            return self._board[y + offset][x + offset]

    def _check_four_in_a_row(self, player: Player, x: int, y: int) -> bool:
        direction_offset_funcs: list[typing.Callable[[int, int, int], Player | None]] = [
            self._get_value_with_horizontal_offset,
            self._get_value_with_vertical_offset,
            self._get_value_with_diagonal_bottom_left_to_top_right_offset,
            self._get_value_with_diagonal_top_left_to_bottom_right_offset,
        ]

        for offset_func in direction_offset_funcs:
            contiguous_count = 1  # current location should already be the current player.
            check_up = check_down = True

            for offset in range(1, 5):
                if check_up and offset_func(x, y, offset) == player:
                    contiguous_count += 1
                else:
                    check_up = False

                if check_down and offset_func(x, y, -offset) == player:
                    contiguous_count += 1
                else:
                    check_down = False

            if contiguous_count >= 4:
                return True

        return False

    def do_move(self, player: Player, x: int) -> bool:  # player is '1' or '2', x is the variable where the outcome of the get_move
                                                        # fuction was assigned to on line 108, an int from 0 to 6

        for n in range(self._height):                   # set up 6 itters over the y-axle and check the x-coordinate on every y-axle
            if self._board[n][x] is not None:           # when, on the itteration n from top to bottom, and on the x-column we check (column we check is the int we got from get_move)
                y = n - 1                               # the value is not None, the y-x coordinate is taken by a player allready. We then want to place our player number
                break                                   # on that y-coordinate one row higher, so the itter we are in minus 1. We now have the y-coordinate and break the for loop
        else:
            y = self._height-1                          # if no not None on any of the itters from the for loop we reach itter 6 and know we use the index[itter - 1] is index 5 as y coordinate

        self._board[y][x] = player                      # we now assign the '1' or '2' from player to that y-x coordinate on the board
        return self._check_four_in_a_row(player, x, y)  # as a return value we return the self, calling on the check_fiar function with the player ('1' or '2') and the x/y-coordinates
                                                        # move to line 48
    def display_board(self) -> None:
        print('+0-1-2-3-4-5-6-+')
        for row in self._board:                         # 6 itters 
            print('|', end='')                          # print 6 | from top tp bottom
            for column in row:                          # after each | 7 itters over the still Nones
                if column is None:                      # for every None we find, print "square" and space 
                    print('☐', end=' ')
                else:                                   # if it's not None it is allready a "square"
                    print(column, end=' ')              # so print the "square" that's in there and space
            print('|')                                  # end each row with a |
        print('+0-1-2-3-4-5-6-+')                       # func finished, move to line 94


class ConnectFourGame:
    _BOARD_WIDTH = 7
    _BOARD_HEIGHT = 6

    def __init__(self) -> None:
        self._board = Board(self._BOARD_WIDTH, self._BOARD_HEIGHT)                      # make an instance of the board class with width of 7 columns and height of 6 rows
                                                                                        # with 7 * 6 None values, this outlines the seize of the empty board
        self._players = [Player('1'), Player('2')]                                      # make 1 instance of the Player class for 2 players, class attribute '1' and the same for '2'

    def _get_move(self, player: Player) -> int:                                         # var player is "1"
        print(f'<== Player {player}\'s turn ==> ')                                      # print player 1's turn
        self._board.display_board()                                                     # call the display_board function on the empty but outlined self.board , move to line 67
        input_row = 'None'                                                              # because we do a value check on line 96 we use this snippet to activate the snippet starting on line 97
                                                                                        # every time we call the get_move it is set to "None" again

        while not input_row.isdigit() or not 0 < int(input_row) < self._BOARD_WIDTH:    # as long as the input_row is not a digit (it is "None" at this point)
                                                                                        # or the input row is not bigger or equal to 0 or not smaller than the width(7):    
            input_row = input(f'Please pick a row (0-{self._BOARD_WIDTH-1}):')          # print this line "pick a row (0 - (7-1))"  (repeat on wrong input)
                                                                                        # first time it triggers on the "None" from line 94, after that it keeps triggering 
                                                                                        # if input is not digit from 0 to 6
        return int(input_row)                                                           # returns the input, wich is a string, as an int, back to line 108

    def run_game(self) -> None:
        turn_counter = 0                                            # start with turn_counter 0
        current_player = self._players[turn_counter]                # we assign the index 0 of self._player ,('1'), to player
        x = self._get_move(current_player)                          # we assign the function call get_move() with var '1' to x (x is the x-axle on the board, handy), move to line 89
        while not self._board.do_move(current_player, x):
            turn_counter += 1
            current_player = self._players[turn_counter % 2]
            x = self._get_move(current_player)
        print('!!! CONGRATULATIONS !!!')
        print(f'!!! PLAYER {current_player} WON !!!')
        self._board.display_board()


if __name__ == '__main__':
    game = ConnectFourGame()                # make an instance of the ConnectFourGame() class
    game.run_game()                         # start the game by calling the run_game method on the class, move to line 124