'''
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n^2) per move() operation?
'''
# O(n) per move(), but use O(n^2) space
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.matrix = [[0 for i in range(n)] for j in range(n)]
        self.winning = False

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if self.winning == True:
            return
        self.matrix[row][col] = player
        n = len(self.matrix)
        indicator = True
        for i in range(n):
            if self.matrix[row][i] != player:
                indicator = False
                break
        if indicator == True:
            self.winning = True
            return player
        
        indicator = True
        for i in range(n):
            if self.matrix[i][col] != player:
                indicator = False
                break
        if indicator == True:
            self.winning = True
            return player
        
        if row == col:
            indicator = True
            for i in range(n):
                if self.matrix[i][i] != player:
                    indicator = False
                    break
            if indicator == True:
                self.winning = True
                return player
        if row + col == n - 1:
            indicator = True
            for i in range(n):
                if self.matrix[i][n - 1 - i] != player:
                    indicator = False
                    break
            if indicator == True:
                self.winning = True
                return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# space: O(n), time: O(1)
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row = [0] * n
        self.col = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0
        self.winning = False

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if self.winning == True:
            return
        if player == 1:
            val = 1
        else:
            val = -1
        self.row[row] += val
        self.col[col] += val
        if row == col:
            self.diagonal += val
        n = len(self.row)
        if row + col == n - 1:
            self.antidiagonal += val
        if abs(self.row[row]) == n or abs(self.col[col]) == n or abs(self.diagonal) == n or abs(self.antidiagonal) == n:
            self.winning = True
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

