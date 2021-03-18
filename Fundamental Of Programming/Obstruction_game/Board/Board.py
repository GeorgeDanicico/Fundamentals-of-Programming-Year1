"""
The board will be represented as a list of lists but it will be printed as a Texttable

The user can set the dimensions of the board at the beginning of the game

In the board class we will have
    - move_validation
    - printing the board as a Texttable
    - method to get the board


At the beginning all the elements are None. If the user makes a move, his square will be marked by an 'X' and the computers move
will be marked by an 'O'
"""
from tkinter import DISABLED

from texttable import Texttable

class Board:
    def __init__(self, rows, columns):
        """
        :param rows: the number of rows entered by the user
        :param columns: the number of columns entered by the user
        """
        self._rows = rows
        self._columns = columns

        # we initialise the
        self._board = [[None for j in range(self._columns)] for i in range(self._rows)]
        self._number_of_empty_spaces = rows * columns

    def __str__(self):
        t = Texttable()
        head_list = [' ']
        for i in range(self._columns):
            head_list.append(str(i))
        t.header(head_list)

        for row in range(self._rows):
            row_data = []

            for element in self._board[row]:
                if element is None:
                    row_data.append(' ')
                if element == 'X' or element == 'O':
                    row_data.append(element)
                if element == 1:
                    row_data.append('-')

            t.add_row([row] + row_data)

        return t.draw()

    @property
    def number_empty_spaces(self):
        """
        we return the number of empty spaces because we need to know when the game is over
        """
        return self._number_of_empty_spaces

    def empty_cells(self):
        # A list of all the empty cells on the board will be returned
        cells = []
        for i in range(self._rows):
            for j in range(self._columns):
                if self.get_element(i, j) is None:
                    cells.append([i, j])
        return cells

    def valid_coordinates(self, x, y):
        return 0 <= x < self._rows and self._columns > y >= 0

    def check_coordinates(self, x, y):
        if x != int(x) or y != int(y):
            raise Exception("Invalid move!...\n")
        if x not in range(0, self._rows) or y not in range(0, self._columns):
            raise Exception("Invalid move!... Out of the board...\n")
        if self._board[x][y] is not None:
            raise Exception("Square already taken!...\n")

    def get_element(self, x, y):
        """
        the element can be:
            - 'X' if it was a users move
            - 'O' if it was a computers move
            - '-' if the square was used
            - 'None' if the square is empty
        :return: the element on the position x, y
        """
        return self._board[x][y]

    def move(self, x, y, symbol):
        """
        we set all the empty squares related to that position
        :param x, y: the coordinates of the move
        :param symbol: it will be 'X' if its the users turn/ 'O' if it will be the computers turn
        """
        # we check if the coordinates lead to an empty square

        self.check_coordinates(x, y)
        self._board[x][y] = symbol
        self._number_of_empty_spaces -= 1
        for i in range(3):
            if self.valid_coordinates(x - 1, y - 1 + i):
                if self._board[x - 1][y - 1 + i] != 1:
                    self._board[x - 1][y - 1 + i] = 1
                    self._number_of_empty_spaces -= 1
            if self.valid_coordinates(x + 1, y - 1 + i):
                if self._board[x + 1][y - 1 + i] != 1:
                    self._board[x + 1][y - 1 + i] = 1
                    self._number_of_empty_spaces -= 1
        if self.valid_coordinates(x, y - 1):
            if self._board[x][y - 1] != 1:
                self._board[x][y - 1] = 1
                self._number_of_empty_spaces -= 1
        if self.valid_coordinates(x, y + 1):
            if self._board[x][y + 1] != 1:
                self._board[x][y + 1] = 1
                self._number_of_empty_spaces -= 1

    def gui_move(self, x, y, symbol, gui_button_list):
        """
        The function is similar to the basic move function, It changes depending on the move
            the state and the color of the buttons.
        It doesnt need validations because it will be called only after the first move function,
            if it will be executed succesfully
        """

        gui_button_list[x][y]["bg"] = "red" if symbol == 'X' else "blue"
        gui_button_list[x][y]["state"] = DISABLED
        for i in range(3):
            if self.valid_coordinates(x - 1, y - 1 + i):
                if gui_button_list[x - 1][y - 1 + i]["bg"] == "white":
                    gui_button_list[x - 1][y - 1 + i]["bg"] = "gray"
                    gui_button_list[x - 1][y - 1 + i]["state"] = DISABLED
            if self.valid_coordinates(x + 1, y - 1 + i):
                if gui_button_list[x + 1][y - 1 + i]["bg"] == "white":
                    gui_button_list[x + 1][y - 1 + i]["bg"] = "gray"
                    gui_button_list[x + 1][y - 1 + i]["state"] = DISABLED
        if self.valid_coordinates(x, y - 1):
            if gui_button_list[x][y - 1]["bg"] == "white":
                gui_button_list[x][y - 1]["bg"] = "gray"
                gui_button_list[x][y - 1]["state"] = DISABLED
        if self.valid_coordinates(x, y + 1):
            if gui_button_list[x][y + 1]["bg"] == "white":
                gui_button_list[x][y + 1]["bg"] = "gray"
                gui_button_list[x][y + 1]["state"] = DISABLED

