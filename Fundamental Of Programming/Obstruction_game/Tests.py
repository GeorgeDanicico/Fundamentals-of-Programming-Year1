from unittest import TestCase
from Board.Board import Board
from Game.Game import Game


class Test_Game(TestCase):
    def test_board(self):
        board = Board(6, 6)

        board.move(1, 1, 'X')
        board.move(4, 2, 'O')
        self.assertEqual(board.number_empty_spaces, 18)
        self.assertEqual(len(board.empty_cells()), 18)
        try:
            board.move(4, 1, 'X')
            self.assertFalse('not ok')
        except Exception:
            self.assertTrue('ok')

    def test_Game(self):
        game = Game(6, 6, 'X', 'O')

        game.board.move(1, 1, 'X')
        game.board.move(1, 5, 'O')
        game.board.move(4, 1, 'X')
        game.computer_move()

        self.assertEqual(len(game.board.number_empty_spaces), 0)
