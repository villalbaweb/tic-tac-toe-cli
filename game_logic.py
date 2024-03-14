from helpers import Helpers
from game_board import GameBoard

helpers = Helpers()
game_board = GameBoard()

class GameLogic():
    def __init__(self) -> None:
        self.use_first = True
        self.symbols = [ 'X', 'O' ]

    def play_game(self) -> bool:
        selected_symbol = self.symbols[0] if self.use_first else self.symbols[1]

        coordinate_text = input(f'Make {selected_symbol} turn, enter cordinate (row, col) coma separated: ')

        coordinate_tuple = helpers.get_coordinate_tuple(coordinate_text)

        board_updated: bool = game_board.add_move(selected_symbol, coordinate_tuple)

        if board_updated:
            self.use_first = not self.use_first
        else:
            print('Wrong position entered, try again...')

        game_board.display_board()

        if game_board.win_movement():
            print(f'Player {selected_symbol} wins')
            return True
        elif game_board.check_draw():
            print(f'Draw game!')
            return True

        return False