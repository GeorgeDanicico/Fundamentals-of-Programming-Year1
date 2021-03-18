import random
from texttable import Texttable


class Board:
    def __init__(self, dimension, number_of_apple):
        self._dimension = dimension
        self._board = [[None for i in range(dimension)] for j in range(dimension)]
        self._number_of_apple = number_of_apple
        # There will be possible dimension ^ 2 / 2 adjacent solutions for apple because the snake is place in the middle
        self._free_spaces = (dimension ** 2) / 2
        self._snake_position = []
        # we place the snake
        self.place_snake()
        self.generate_random_apples(self._number_of_apple)

    @property
    def get_dimension(self):
        return self._dimension

    @property
    def snake_pos(self):
        return self._snake_position

    def get_cell(self, row, column):
        return self._board[row][column]

    def adjacent_apple(self, row, column):
        if row < 0 or row >= self._dimension or column < 0 or self._dimension <= column:
            return True
        return 0 <= row < self._dimension and 0 <= column < self._dimension and (self._board[row][column] is None)

    def __str__(self):
        table = Texttable()
        for row in range(self._dimension):
            row_data = []
            for column in range(self._dimension):
                if self._board[row][column] == '1':
                    row_data.append('*')
                elif self._board[row][column] == '2':
                    row_data.append('+')
                elif self._board[row][column] == '3':
                    row_data.append('.')
                else:
                    row_data.append(' ')
            table.add_row(row_data)

        return table.draw()

    def place_snake(self):
        column_placing = self._dimension // 2
        # this will be the coordinates of the head
        row_placing = (self._dimension - 3) // 2

        self._snake_position.append([row_placing, column_placing])
        self._snake_position.append([row_placing + 1, column_placing])
        self._snake_position.append([row_placing + 2, column_placing])

        self._board[row_placing][column_placing] = '1'
        self._board[row_placing + 1][column_placing] = '2'
        self._board[row_placing + 2][column_placing] = '2'

    def generate_random_apples(self, number):
        """
        This function tries to generate a number of apples that can fit on the board
        :param number: the number of apples that needs to be generated
        """
        # counter will be increased every time there hasnt been generated a good apple
        # we assume that if counte reach 20000 tries, it means that there is no possible placement for another apple
        counter = 0

        while number:
            row = random.randint(0, self._dimension - 1)
            column = random.randint(0, self._dimension - 1)
            if self._board[row][column] is None and self.adjacent_apple(row + 1, column) and self.adjacent_apple(row - 1, column) and self.adjacent_apple(row, column + 1) and self.adjacent_apple(row, column - 1):
                self._board[row][column] = '3'
                number -= 1
                counter = 0
            else:
                counter += 1

            if counter == 20000:
                break

    def reset_board(self):
        """
        This function 'resets the board', basically it just deletes all the previous positions of the snake
        """
        for i in range(self._dimension):
            for j in range(self._dimension):
                if self._board[i][j] == '1' or self._board[i][j] == '2':
                    self._board[i][j] = None

    def set_new_board(self, new_positions):
        """
        This function sets the new snake positions for the
        :param new_positions: the list of the new positions of the snake
        """
        self._snake_position = new_positions
        length = len(new_positions)
        self._board[new_positions[0][0]][new_positions[0][1]] = '1'
        for i in range(1, length):
            self._board[new_positions[i][0]][new_positions[i][1]] = '2'
