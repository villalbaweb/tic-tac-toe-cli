board = [
    [ ' ', ' ', ' ' ],
    [ ' ', ' ', ' ' ],
    [ ' ', ' ', ' ' ] 
]

class GameBoard():

    def __init__(self) -> None:
        self.game_board = board

    def display_board(self):
        for row in board:
            row_print = ''
            for col in row:
                row_print += f' {col} |'
            print(f'{row_print}\n------------')
        print('**************\n')

    def add_move(self, symbol: str, position: tuple) -> bool:

        row_ix = position[0] - 1
        col_ix = position[1] - 1
        
        if row_ix < 0 or row_ix > 2 or col_ix < 0 or col_ix > 2: return False
        
        if self.game_board[row_ix][col_ix] != ' ': return False

        self.game_board[position[0] - 1][position[1] - 1] = symbol

        return True
    
    def win_movement(self) -> bool:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ' or \
            board[0][i] == board[1][i] == board[2][i] != ' ':
                return True

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != ' ' or \
        board[0][2] == board[1][1] == board[2][0] != ' ':
            return True

        return False
    
    def check_draw(self):
        for row in self.game_board:
            if ' ' in row:
                return False

        return True