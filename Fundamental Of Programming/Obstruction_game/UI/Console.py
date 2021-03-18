from Game.Game import Game
import psycopg2


class Console_UI:
    """
    when the game start, it asks the user for the dimensions of the board and the \
    symbol he want to take
    """
    def __init__(self):
        self._rows = None
        self._columns = None
        self._game_board = None
        self._user_sign = None
        self._computer_sign = None

    def read_starting_game_data(self):
        correct_data = False
        while not correct_data:
            try:
                rows = input("Please enter the number of rows of the board: ").strip()
                if not rows.isdigit():
                    raise Exception("Invalid character for rows!...")
                columns = input("Please enter the number of columns of the board: ").strip()
                if not columns.isdigit():
                    raise Exception("Invalid character for columns!...")
                if int(rows) > 8 or int(columns) > 8:
                    raise Exception("Numbers too big for the size of the board!...")

                user_sign = input("Please enter the sign you want to play with (X/O): ").strip()
                if user_sign not in ['X', 'O']:
                    raise Exception("Invalid sign entered!...")

                self._rows = int(rows)
                self._columns = int(columns)
                self._user_sign = user_sign
                correct_data = True
            except Exception as message:
                print(str(message) + '\n')

        if self._user_sign == 'X':
            self._computer_sign = 'O'
        else:
            self._computer_sign = 'X'

        self._game_board = Game(self._rows, self._columns, self._user_sign, self._computer_sign)

    def start(self):
        # The user should be able to play as many rounds against the bot as he wants
        in_game = True
        user_name = input("Welcome! Please enter your name: ").strip()
        user_score = 0
        computer_score = 0
        is_registered = False
        print('\n')
        # If the user has already played in the past, his score is recorded in the data base

        connection_string = psycopg2.connect("host=localhost dbname=postgres user=postgres password=polopolo")
        current_connector = connection_string.cursor()
        current_connector.execute("select * from player")
        # If the user is present in the data base, is_registered will be True/False otherwise
        # This will help at the end of the game, because if is_regitered == False it means the user must be placed in the database
        # if is_registered == True it means that the user score must be updated
        for row in current_connector:
            if user_name == str(row[0]):
                is_registered = True
                user_score = int(row[1])
                computer_score = int(row[2])

        while in_game:

            self.read_starting_game_data()
            finished = False
            human_turn = False
            if self._user_sign == 'O':
                human_turn = True

            while not finished:
                # firstly, the computer does the move
                if human_turn:

                    correct_user_move = False
                    while not correct_user_move:
                        row_index = input("Enter the row: ").strip()
                        column_index = input("Enter the column: ").strip()

                        if row_index.isdigit() and column_index.isdigit():
                            try:
                                self._game_board.user_move(int(row_index), int(column_index))
                                correct_user_move = True
                            except Exception as error_message:
                                print(str(error_message) + '\n')
                    print(self._game_board.board)
                    human_turn = False
                else:
                    correct_move = False
                    while not correct_move:
                        try:
                            bot_row, bot_column = self._game_board.computer_move()
                            print(f"The computers move is: [{bot_row}, {bot_column}]")
                            correct_move = True
                        except Exception:
                            pass
                    print(self._game_board.board)
                    human_turn = True

                print("\n")

                if self._game_board.board.number_empty_spaces == 0:
                    """
                    this means that the game ended
                        - if the human_turn = True, it means that the last move was done by the computer
                        and it means that the computer won.
                        - if the human_turn = False, it means that the last move was done by the 
                        user and it means that the user won.
                    """
                    finished = True

            if human_turn is False:
                print("Congratulation, you won!")
                user_score += 1
            else:
                print("Unfortunately, you lost...")
                computer_score += 1

            if is_registered is False:
                current_connector.execute("Insert into player values (%s, %s)", (user_name, user_score))
                is_registered = True
            else:
                current_connector.execute("update player set player_score = %s where player_name = %s",
                                          (user_score, user_name))
                current_connector.execute("update player set computer_score = %s where player_name = %s",
                                          (computer_score, user_name))

            connection_string.commit()

            print(f"CPU: {computer_score} |  {user_name}: {user_score}\n")
            play_again = input("Do you want to play again? ").strip()
            print("\n")
            if play_again.lower() != "yes":
                in_game = False

        current_connector.close()
        connection_string.close()