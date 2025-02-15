from typing import List

winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # columns

    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # rows

    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
    # diagonals
]

class TicTacToe:
    _board: List[List[int]]
    """
    0 - empty, 1 - O, 2 - X
    """
    _o_to_move: bool
    _game_over: bool
    _size: int

    def __init__(self):
        self._board = [[0 for _ in range(3)] for _ in range(3)]
        self._o_to_move = True
        self._game_over = False
        self._size = 3
        
    @property
    def board(self) -> List[List[int]]:
        return self._board
    
    @property
    def o_to_move(self) -> bool:
        return self._o_to_move
    
    def restart(self):
        self._board = [[0 for _ in range(3)] for _ in range(3)]
        self._o_to_move = True


    def move(self, x: int, y: int) -> int:
        """
        place a move on the board, return 1 if success and 0 if failed
        """
        if x < 0 or x >= self._size or y < 0 or y >= self._size:
            return 0
        
        if self._game_over:
            return 0
        
        if self._board[x][y] != 0:
            return 0
        
        
        self._board[x][y] = 1 if self._o_to_move else 2
        self._o_to_move = not self._o_to_move

        return 1
    
    def check_winner(self) -> int:
        """
        return 0 if no winner, 1 if O won, 2 if X won
        """
        for combination in winning_combinations:
            if all(self._board[x][y] == 1 for x, y in combination):
                self._game_over = True
                return 1
            if all(self._board[x][y] == 2 for x, y in combination):
                self._game_over = True
                return 2
        
        if all(self._board[x][y] != 0 for x in range(3) for y in range(3)):
            return 3
        return 0