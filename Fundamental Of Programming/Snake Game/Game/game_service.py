class ServiceException(Exception):
    def __init__(self, msg):
        self._msg = msg


class Game:
    def __init__(self, board):
        self._board = board
        self._direction = 'up'

    @property
    def board(self):
        return self._board

    def check_out(self, row, column):
        if row < 0 or column < 0 or row >= self.board.get_dimension or column >= self.board.get_dimension:
            return False
        return True

    def move_one_step(self):
        """
        This function will make a move in the direction that was setted
        If there was no direction setted, the implicit one is 'up'
        :return:
        :rtype:
        """
        positions = self.board.snake_pos

        snake_length = len(positions) - 1
        last_cell = positions[snake_length][:]

        new_positions = []
        head = []
        # There are 4 possible directions in which we can go
        # 1. If we want to go up the head changes on row by decreasing with 1
        # 2. If we want to go down the head changes on row by increasing with 1
        # 3. If we want to go right, the head changes on the colmun by increasing with 1
        # 4. If we want to go left, the head changes on the colmun by decreasing with 1
        if self._direction == 'up':
            head = positions[0][:]
            head[0] -= 1
            new_positions.append(head)

        if self._direction == 'down':
            head = positions[0][:]
            head[0] += 1
            new_positions.append(head)

        if self._direction == 'left':
            head = positions[0][:]
            head[1] -= 1
            new_positions.append(head)

        if self._direction == 'right':
            head = positions[0][:]
            head[1] += 1
            new_positions.append(head)

        # If the snake went out of the board, we raise an Exception to warn the user!
        if self.check_out(head[0], head[1]) is False:
            raise ServiceException("Ups, the snake hits the wall!...")

        for cell_index in range(0, snake_length):
            new_positions.append(positions[cell_index][:])
        # If the snake head touched its tail, the game is over.
        if self.board.get_cell(new_positions[0][0], new_positions[0][1]) == '2':
            raise ServiceException("The snake tried to eat himself!...\n")

        # If the snake ate an apple, it means that its tail must increase by 1
        if self.board.get_cell(new_positions[0][0], new_positions[0][1]) == '3':
            new_positions.append(last_cell)
            self.board.generate_random_apples(1)

        # we reset the board, and then complete it again with new positions
        self.board.reset_board()
        self.board.set_new_board(new_positions)

    # The below function changes the directions
    def set_direction(self, new_direction):
        if (self._direction == 'up' and new_direction == 'down') or (self._direction == 'down' and new_direction == 'up'):
            raise ServiceException('Invalid 180 degree move.\n')
        if (self._direction == 'left' and new_direction == 'right') or (self._direction == 'right' and new_direction == 'left'):
            raise ServiceException('Invalid 180 degree move.\n')

        if self._direction != new_direction:
            self._direction = new_direction
            self.move_one_step()
