class Board:
    '''
    This class creates the game board and defines the rules for making turns and when the game is won.
    '''
    def __init__(self):
        '''
        TicTacToe game board
        '''

        self.state = [0,0,0,0,0,0,0,0,0]

    def make_turn(self, cell, player):
        '''
        This method defines the winning conditions

        Args: player ():
              cell (INT): to mark postion on the game board

        Returns: True
        '''

        if self.is_valid_turn(cell):
            self.state[cell] = player.symbol
            return True
        return False

    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False

    def check_win(self, player):
        '''
        This method defines the winning conditions

        Args: player (INT): Defines the symbol

        Returns: True
        '''

        s = player.symbol

        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True

    def is_full(self):
        '''
        This method checks if there are still free spaces on the game board

        Args: None

        Returns: None
        '''

        for i in self.state:
            if i == 0:
                return False
        return True

    def print_sign(self, sign):
        '''
        This method prints the sign of the player on the game board

        Args: sign (INT): representing the player, 1 = X, -1 = O

        Returns: 'X' or 'O'
        '''

        if sign == 0:
            return '-'
        elif sign == 1:
            return 'X'
        else:
            return 'O'

    def print_board(self):
        '''
        This method prints the board layout

        Args: None

		Returns: None
        '''
        print(' ' + self.print_sign(self.state[0]) + ' | ' + self.print_sign(self.state[1]) + ' | ' + self.print_sign(self.state[2]) + ' \n' +
              ' ' + self.print_sign(self.state[3]) + ' | ' + self.print_sign(self.state[4]) + ' | ' + self.print_sign(self.state[5]) + ' \n' +
              ' ' + self.print_sign(self.state[6]) + ' | ' + self.print_sign(self.state[7]) + ' | ' + self.print_sign(self.state[8]) + ' ')
