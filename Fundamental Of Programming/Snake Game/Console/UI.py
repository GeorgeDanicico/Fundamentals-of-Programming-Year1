from Game.game_service import ServiceException


class UI:

    @staticmethod
    def print_menu():
        print("move [n] - moves the snake n positions, if n isn't specified it moves one position")
        print("up/left/right/down - changes the direction of the snake\n")

    def __init__(self, game):
        self._game_service = game

    def make_a_move(self, parameters):
        if len(parameters) == 1:
            # it means that we will move the snake only one time
            self._game_service.move_one_step()
        else:
            number_of_moves = int(parameters[1])
            while number_of_moves:
                self._game_service.move_one_step()
                number_of_moves -= 1

        self.print_board()

    def change_direction(self, command):
        try:
            new_direction = command[0].strip()
            self._game_service.set_direction(new_direction)
            self.print_board()
        except ServiceException as ve:
            print(str(ve))
            self.print_board()

    def print_board(self):
        print(self._game_service.board)

    def start(self):
        done = False

        command_dict = {'move': self.make_a_move,
                        'up': self.change_direction,
                        'right': self.change_direction,
                        'left': self.change_direction,
                        'down': self.change_direction
                        }
        print("Snake Game V1.0")
        self.print_board()
        while not done:
            UI.print_menu()
            try:
                command = input("Enter the command please: ").lower()
                command = command.split(' ')
                if command[0] in command_dict:
                    command_dict[command[0]](command)
                else:
                    print("Invalid command entered!...\n")
            except ServiceException as ve:
                print(str(ve))
                done = True
                print("GAME OVER!")
            except Exception as ve:
                print(str(ve))
                done = True
                print("GAME OVER!")


