from app.game import TicTacToe

def test_init():
    game = TicTacToe()
    assert game.board == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert game._o_to_move == True
    assert game._game_over == False

def test_move():
    game = TicTacToe()
    assert game.o_to_move == True
    assert game.move(0, 0) == 1
    assert game.board[0][0] == 1

    assert game.o_to_move == False
    assert game.move(0, 0) == 0
    assert game.board[0][0] == 1

    assert game.move(0, 1) == 1
    assert game.board[0][1] == 2
    assert game.o_to_move == True
    assert game.move(0, 1) == 0

    assert game.move(3, 0) == 0
    assert game.o_to_move == True

def test_restart():
    game = TicTacToe()
    game.move(0, 0)

    game.restart()

    assert game.board == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert game.o_to_move == True
    assert game._game_over == False

def test_win_rows():
    game = TicTacToe()
    game.move(0, 0)
    game.move(1, 0)
    game.move(0, 1)
    game.move(1, 1)
    game.move(0, 2)
    assert game.check_winner() == 1
    assert game._game_over == True


def test_win_diagonals():
    game = TicTacToe()

    game.move(1, 0)
    game.move(0, 0)
    game.move(2, 0)
    game.move(1, 1)
    game.move(0, 1)
    game.move(2, 2)
    assert game.check_winner() == 2
    assert game._game_over == True

def test_win_columns():
    game = TicTacToe()
    game.move(0, 0)
    game.move(0, 1)
    game.move(1, 0)
    game.move(1, 1)
    game.move(2, 0)

    assert game.check_winner() == 1
    assert game._game_over == True


