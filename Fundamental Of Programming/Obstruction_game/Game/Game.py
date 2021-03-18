from Board.Board import Board
from Strategy.Strategy import Strategy


class Game:
    def __init__(self, rows, columns, user_sign, computer_sign):
        self._board = Board(rows, columns)
        self._strategy = Strategy()
        self._user = user_sign
        self._comp = computer_sign

    @property
    def board(self):

        return self._board

    def user_move(self, x, y):
        self._board.move(x, y, self._user)

    def computer_move(self):
        cpu_move = self._strategy.minimax_algorithm(self._board, self._user, self._comp)
        self._board.move(cpu_move[0], cpu_move[1], self._comp)
        return cpu_move[0], cpu_move[1]
        print(f"The computers move is: [{cpu_move[0]}, {cpu_move[1]}]")
        # it will call a method from the strategy class when it is finished
