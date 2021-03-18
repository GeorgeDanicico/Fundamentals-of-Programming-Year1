"""
The idea of the minimax algorithm is that it will choose always the best suited cell in order to "win" faster

It is a "backtracking" algorithm, we take all possible solutions, and after that, in this case
it will choose the first one with a minimal number of steps until the win
"""
from copy import deepcopy
import random

class Strategy:
    # this function will evaluate our current board and will return True if the computer
    # is one step away from victory/ False otherwise
    def evaluate_board(self, board, empty_cells, symbol):
        """
        :param board: The current board for the game
        :param empty_cells: The list of coordinates for every empty square at that time
        :param symbol: the symbol of the computer
        :return : True, cell if there was a winning move/ False, None if there isnt a one winning move
        """
        # cell is a list [row, column] where row is the row index and column is the column index
        for cell in empty_cells:

            board_copy = deepcopy(board)
            board_copy.move(cell[0], cell[1], symbol)
            # if after a move by the computer there are no empty spaces => this is the computer winning move
            if board_copy.number_empty_spaces == 0:
                return True, cell
        return False, None

    def minimax_algorithm(self, board, user_sign, comp_sign):
        """
        we check if there is a one winning move and if not, we find the best move
        :param board: The current board of the game
        :param user_sign: the user symbol
        :param comp_sign: the sign of the computer
        :return:
        """
        empty_cells = board.empty_cells()
        statement, cell = self.evaluate_board(board, empty_cells, comp_sign)
        if statement is True:
            return cell
        # we find the best move for the cpu
        next_AI_move = self.find_best_move(board, empty_cells, user_sign, comp_sign)
        return next_AI_move

    def find_best_move(self, board, empty_cells, user_sign, comp_sign):
        # at the beginning we set the depth and the best_move with None
        best_move_depth = None
        best_move = None

        # we parse through all the empty cells of the board
        for cell in empty_cells:
            board_copy = deepcopy(board)
            current_cell = None
            score, count = 0, 0

            # now we go through the empty cells and fill the board
            # always the computer will have the first move
            while score == 0:
                if count % 2 == 0:
                    symbol = comp_sign
                else:
                    symbol = user_sign

                board_copy.move(cell[0], cell[1], symbol)
                count += 1
                if board_copy.number_empty_spaces == 0:
                    # if the board was filled and the last move was done by the cpu
                    # if the score is positive it means that the cpu has won/ otherwise the user has won
                    # The cpu is in this case the maximizer and the user is the minimizer
                    if (count - 1)% 2 == 0:
                        score = 10
                        current_cell = cell
                    else:
                        score = -10
                else:
                    # if the board wasn't completely filled, we randomly pick a new cell from the new list of the empty cells
                    new_list = board_copy.empty_cells()
                    cell = new_list[random.randint(0, len(new_list) - 1)]
                    # cell = board_copy.empty_cells()[0]

            # if there was no move before, we set it with the current_cell
            # NB! It can be also None if the winner resulted in the loop was the user!
            if best_move_depth is None:
                best_move_depth = count
                best_move = current_cell
            elif count < best_move_depth:
                best_move_depth = count
                best_move = current_cell

        # if there is a best_move we return it/ otherwise we generate randomly one from the empty cells list.
        if best_move is not None:
            return best_move
        else:
            # best_move = empty_cells[random.randint(0, len(empty_cells) - 1)]
            best_move = empty_cells[0]
            return best_move

