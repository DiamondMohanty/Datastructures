# Develop a tic tac toe game getting input from command line
# Author: Diamond Mohanty
# Date: 04-Jan-2022

class TicTacToe():
    def __init__(self) -> None:
        self._board_size = 3
        self._board = [[''] * self._board_size for _ in range(self._board_size)]
        self._current_player = 'O'

    def display_board(self) -> None:
        for row in range(self._board_size):
            for col in range(self._board_size):
                if col == self._board_size - 1:
                    end = '|'
                else:
                    end = ''
                print("| {0: <3}".format(self._board[row][col]), end=end)
            print()
    def mark(self, cell):

        row = cell[0]
        col = cell[1]
        # Checking if the cell is empty
        if self._board[row][col] != '':
            raise ValueError('Place already occupied')
        
        # Checking the limit of the board
        if row > 2 or row < 0 or col > 2 or col < 0:
            raise ValueError('Out of bounds')

        if self._current_player == 'O':
            self._current_player = 'X'
        else:
            self._current_player = 'O'

        mark = self._current_player
        
        # All Check passed
        self._board[row][col] = mark
        
    def winner(self):

        if self.__isfull__():
            return 'Tie'

        if self.__finished__():
            return self._current_player
        
        return None

    def __isfull__(self):
        '''
            Checks if there is any empty cell in the board
        '''
        full = 0
        for row in range(self._board_size):
            for col in range(self._board_size):
                if self._board[row][col] != '':
                    full += 1
            
        if full == self._board_size * self._board_size:
            return True
        else:
            return False

    def __finished__(self):
        return ((self._board[0][0] != '' and (self._board[0][0] == self._board[0][1] == self._board[0][2])) or # row 1 
           (self._board[1][0] != '' and (self._board[1][0] == self._board[1][1] == self._board[1][2]))  or # row 2
           (self._board[2][0] != '' and (self._board[2][0] == self._board[2][1] == self._board[2][2]))  or # row 3
           (self._board[0][0] != '' and (self._board[0][0] == self._board[1][0] == self._board[2][0]))  or # col 1
           (self._board[0][1] != '' and (self._board[0][1] == self._board[1][1] == self._board[2][1]))  or # col 2
           (self._board[0][2] != '' and (self._board[0][2] == self._board[1][2] == self._board[2][2]))  or # col 3
           (self._board[0][0] != '' and (self._board[0][0] == self._board[1][1] == self._board[2][2]))  or # Diag 1
           (self._board[2][0] != '' and (self._board[2][0] == self._board[1][1] == self._board[0][2])))     # Reverse Diag
    
# Driver
game = TicTacToe()
print("===== Game Initialized =====")
while game.winner() is None:
    new_position = input()
    pos1 = int(new_position[0])
    pos2 = int(new_position[1])
    try:
        game.mark((pos1,pos2))
    except ValueError as e:
        print(e)
        continue
    game.display_board()

winner = game.winner()
if winner == 'Tie':
    print('Game ends in a Tie')
else:
    print("{0} wins the game".format(winner))