from tkinter import *
from tkinter import messagebox
import psycopg2
from Game.Game import Game


class GUI:
    """
    The design ideas we're taken from http://www.papg.com/show?2XMX
    """
    @staticmethod
    def insert_empty_space(frame, row, column):
        """
        This function is used to insert empty spaces to make the GUI prettier
        because I hate Tkinter
        :param frame: the frame in which the empty space is inserted
        :param row: the row on which we will grid
        :param column: the column on which we will grid
        """
        empty_label = Label(frame, text="")
        empty_label.grid(row=row, column=column)

    @staticmethod
    def open_database_connection():
        connection_string = psycopg2.connect("host=localhost dbname=postgres user=postgres password=polopolo")
        current_connector = connection_string.cursor()
        return connection_string, current_connector

    @staticmethod
    def close_database_connection(connection_string, current_connector):
        connection_string.commit()
        connection_string.close()
        current_connector.close()

    def __init__(self):
        self.button_cells = []      # This will keep all the buttons in form of a matrix
        self.frame_gameplay = None  # This will be the gameplay frame which will be initialised in start_game function
        self.game = None            # This will be a Game type variable, It will be initialised in start_game because we need the rows/colums of the board
        self.user_score = 0         # This will keep the user score
        self.cpu_score = 0          # This will keep the cpu score
        self.row = 0                # This will keep the number of rows of the board
        self.column = 0             # This will keep the number of columns of the board
        self.user_symbol = None     # This will keep the user symbol
        self.cpu_symbol = None      # This will keep the cpu symbol
        self.human_turn = None      # This will be True if it is human's turn/False otherwise

        self.root = Tk()
        self.root.title("Play obstruction!")
        self.root.geometry("700x400")
        self.root.iconbitmap(
            'C:/Users/georg/OneDrive/Desktop/Informatica/Facultate/a11-912-Danicico-George/obstruction_icon.ico')
        self.frame_game_entry = Frame(self.root, bd=4, highlightbackground="black", height=400, width=700)
        self.frame_game_entry.pack()
        # Implementation of the entry frame for the game
        welcome_label = Label(self.frame_game_entry, text="Play obstruction!")
        welcome_label.grid(row=0, column=0)

        GUI.insert_empty_space(self.frame_game_entry, 1, 0)

        name_label = Label(self.frame_game_entry, text="Your name: ")
        name_label.grid(row=2, column=0)
        # The Entry user_name will be needed when the user will press the New Game button in order to make
        # the connection with the data base
        self.user_name = Entry(self.frame_game_entry)
        self.user_name.grid(row=2, column=1)

        GUI.insert_empty_space(self.frame_game_entry, 3, 0)

        grid_label = Label(self.frame_game_entry, text="Size of grid: ")
        grid_label.grid(row=4, column=0)
        # Implementation for the checkbuttons for the first frame
        # Important! For the size of the grid only one checkbutton can be checked at a time.
        #            The same goes for the choice if the user wants to start the game.
        #           - This is done by the an auxiliary function, which check the variable for the checkbutton and deselect
        #           deselect its state if necessary

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()

        self.size_one = Checkbutton(self.frame_game_entry, text="6x6", command=lambda x=1: self.check_button(x),
                                    variable=self.var1)
        self.size_one.deselect()
        self.size_one.grid(row=4, column=1)

        self.size_two = Checkbutton(self.frame_game_entry, text="7x6", command=lambda x=2: self.check_button(x),
                                    variable=self.var2)
        self.size_two.deselect()
        self.size_two.grid(row=4, column=2)

        self.size_three = Checkbutton(self.frame_game_entry, text="7x7", command=lambda x=3: self.check_button(x),
                                      variable=self.var3)
        self.size_three.deselect()
        self.size_three.grid(row=4, column=3)

        self.size_four = Checkbutton(self.frame_game_entry, text="8x8", command=lambda x=4: self.check_button(x),
                                     variable=self.var4)
        self.size_four.deselect()
        self.size_four.grid(row=4, column=4)
        # --------
        GUI.insert_empty_space(self.frame_game_entry, 5, 0)

        side_label = Label(self.frame_game_entry, text="Do you want to play first? ")
        side_label.grid(row=6, column=0)
        # Set the checkboxes for YES/NO
        # These checkboxes will be needed in order to establish the symbol for the user/computer
        # Always in the game, 'O' will be the symbol for the one who starts, and 'X' for the other

        self.var_yes = IntVar()
        self.var_no = IntVar()

        self.yes_box = Checkbutton(self.frame_game_entry, text="Yes", command=lambda x=5: self.check_button(x),
                                   variable=self.var_yes)
        self.yes_box.deselect()
        self.yes_box.grid(row=6, column=1)

        self.no_box = Checkbutton(self.frame_game_entry, text="No", command=lambda x=6: self.check_button(x),
                                  variable=self.var_no)
        self.no_box.deselect()
        self.no_box.grid(row=6, column=2)

        GUI.insert_empty_space(self.frame_game_entry, 7, 0)

        self.new_game = Button(self.frame_game_entry, text="New Game", command=self.start_game)
        self.new_game.grid(row=8, column=0)

        self.root.mainloop()

    def check_button(self, button):
        """
        This is the auxiliary function we mentioned above. It checks, depending on the button value
        which correspond to a checkbutton, if it was selected to deselect the others.
        :param button: a certain value which is unique for every checkbutton
        """
        if button == 1:
            if int(self.var1.get()) == 1:
                self.size_two.deselect()
                self.size_three.deselect()
                self.size_four.deselect()
        if button == 2:
            if int(self.var2.get()) == 1:
                self.size_one.deselect()
                self.size_three.deselect()
                self.size_four.deselect()
        if button == 3:
            if int(self.var3.get()) == 1:
                self.size_two.deselect()
                self.size_one.deselect()
                self.size_four.deselect()
        if button == 4:
            if int(self.var4.get()) == 1:
                self.size_two.deselect()
                self.size_three.deselect()
                self.size_one.deselect()
        if button == 5:
            if int(self.var_yes.get()) == 1:
                self.no_box.deselect()
        if button == 6:
            if int(self.var_no.get()) == 1:
                self.yes_box.deselect()

    def get_size_of_grid(self):
        """
        Based on the value of the checkbuttons variables, we will return the row/columns for the board
        which will be generated in the gameplay Frame
        :return: row and column of the board
        """
        row = 0
        column = 0
        if int(self.var1.get()) == 1:
            row, column = 6, 6

        if int(self.var2.get()) == 1:
            row, column = 7, 6

        if int(self.var3.get()) == 1:
            row, column = 7, 7

        if int(self.var4.get()) == 1:
            row, column = 8, 8

        return row, column

    def get_symbols(self):
        """
        This function will return the symbols for the user and the cpu
        :return: user symbol and cpu symbol
        NB! Always 'O' does the first move.
        """
        user_symbol, cpu_symbol = None, None
        if int(self.var_yes.get()) == 1:
            user_symbol, cpu_symbol = 'O', 'X'
        elif int(self.var_no.get()) == 1:
            user_symbol, cpu_symbol = 'X', 'O'
        return user_symbol, cpu_symbol

    def start_game(self):
        """
        Below it is initialised the gameplay frame
            - We get from the entry frame:
                - the user name to make the connection with the database
                - the size of the board
                - the symbol for user and cpu / who starts first the game
        """
        user_name = self.user_name.get()
        self.row, self.column = self.get_size_of_grid()
        self.user_symbol, self.cpu_symbol = self.get_symbols()
        if user_name == "" or self.row == 0 or self.user_symbol is None:
            messagebox.showwarning("Warning!", "Please complete all the fields!")
            return
        # The connection to the database in order to rtetrieve the data is done.
        is_registered = False
        connection, cursor = GUI.open_database_connection()
        cursor.execute("select * from player")
        for row in cursor:
            if row[0] == user_name:
                is_registered = True
                self.user_score = int(row[1])
                self.cpu_score = int(row[2])

        if is_registered is False:
            cursor.execute("insert into player values (%s, %s, %s)", (user_name, 0, 0))
        GUI.close_database_connection(connection, cursor)
        # After checking the case if the current user hadn't played the game before, it is added to the database

        self.frame_gameplay = Frame(self.root, bd=4)
        self.frame_game_entry.pack_forget()
        self.frame_gameplay.pack()

        GUI.insert_empty_space(self.frame_gameplay, 0, 10)
        # The purpose of the below labels is for "design
        score_label = Label(self.frame_gameplay, text="Score:")
        score_label.grid(row=0, column=11)

        label_user = Label(self.frame_gameplay, text=user_name)
        label_cpu = Label(self.frame_gameplay, text="CPU")
        label_cpu.grid(row=1, column=12)
        label_user.grid(row=0, column=12)

        lbl_user_score = Label(self.frame_gameplay, text=str(self.user_score))
        lbl_cpu_score = Label(self.frame_gameplay, text=str(self.cpu_score))
        lbl_user_score.grid(row=0, column=13)
        lbl_cpu_score.grid(row=1, column=13)

        funny_label = Label(self.frame_gameplay, text="Play Obstruction!")
        funny_label.grid(row=0, column=0, columnspan=3)

        GUI.insert_empty_space(self.frame_gameplay, 1, 0)
        # The true gameplay starts now!
        self.upload_board()

    def upload_board(self):
        # We clear the buttons list to prevent errors when the user will press the 'play again' button
        # Then, the program generates in form of a matrix with 'row' rows and 'column' colums the buttons
        self.button_cells.clear()
        for i in range(self.row):
            row_cells = []
            for j in range(self.column):
                cell = Button(self.frame_gameplay, bg="white", command=lambda x=i, y=j, z=self.user_symbol: self.prepare_move(x, y, z), padx=12, pady=5)
                row_cells.append(cell)
                cell.grid(row=i + 2, column=j)
            self.button_cells.append(row_cells)

        GUI.insert_empty_space(self.frame_gameplay, self.row+2, 0)
        # the Game variable is created in order to make the moves on the board
        # because behind the scenes lies a simple matrix with ' ', '-', 'X', 'O' symbols
        self.game = Game(self.row, self.column, self.user_symbol, self.cpu_symbol)
        # Because always 'O' starts, we check who starts the game.
        self.human_turn = False if self.user_symbol == 'X' else True

        if self.human_turn is False:
            label_turn = Label(self.frame_gameplay, text="Thinking...")
            label_turn.grid(row=10, column=0, columnspan=2)
            self.prepare_move(None, None, self.user_symbol)
        else:
            label_turn = Label(self.frame_gameplay, text="Your turn...")
            label_turn.grid(row=10, column=0, columnspan=2)

    def prepare_move(self, row, column, symbol):
        """
        This function does a move for the cpu, if it is the cpu's turn
        Othewise it will check if the clicked cell is a valid one by calling "move" and "gui_move" function
        :param row: The row of the clicked cell if it is the human turn/ Otherwise None
        :param column: The column of the clicked cell if it is the human turn/ Otherwise None
        :param symbol: Always the symbol of the user
        """
        if self.human_turn is True:
            # It tries to make the move
            try:
                self.game.board.move(row, column, symbol)
                self.game.board.gui_move(row, column, symbol, self.button_cells)
                self.human_turn = False
                label_turn = Label(self.frame_gameplay, text="Thinking...")
                label_turn.grid(row=10, column=0, columnspan=2)
            except Exception:
                pass
        else:
            cpu_symbol = 'X' if symbol == 'O' else 'O'
            # it generates a random move for the cpu
            correct_move = False
            while not correct_move:
                try:
                    bot_row, bot_column = self.game.computer_move()
                    self.game.board.gui_move(bot_row, bot_column, cpu_symbol, self.button_cells)
                    correct_move = True
                    label_turn = Label(self.frame_gameplay, text="Your turn...")
                    label_turn.grid(row=10, column=0, columnspan=2)
                except Exception:
                    pass
            self.human_turn = True

        # If there are no empty space/ white buttons it means that the game has ended
        # And the winner is the user if human turn is False because the last move was done bu the user
        # Otherwise is the cpu.
        # And also the score labels are updated correspondingly
        if self.game.board.number_empty_spaces == 0:
            if self.human_turn is True:
                messagebox.showinfo("Sorry...", "You cannot defeat a god!")
                label_turn = Label(self.frame_gameplay, text="CPU wins...")
                label_turn.grid(row=10, column=0, columnspan=2)
                self.cpu_score += 1
            else:
                messagebox.showinfo("Congratulations!", "You just won against a god!")
                label_turn = Label(self.frame_gameplay, text="You win :)")
                label_turn.grid(row=10, column=0, columnspan=2)
                self.user_score += 1

            lbl_user_score = Label(self.frame_gameplay, text=str(self.user_score))
            lbl_cpu_score = Label(self.frame_gameplay, text=str(self.cpu_score))
            lbl_user_score.grid(row=0, column=13)
            lbl_cpu_score.grid(row=1, column=13)

            # The database must be with the new scores
            connection, cursor = GUI.open_database_connection()
            cursor.execute("update player set player_score = %s where player_name = %s", (self.user_score, self.user_name.get()))
            cursor.execute("update player set computer_score = %s where player_name = %s", (self.cpu_score, self.user_name.get()))
            GUI.close_database_connection(connection, cursor)
            # After updating the data base, we close the connection
            GUI.insert_empty_space(self.frame_gameplay, 11, 0)

            play_again_button = Button(self.frame_gameplay, text="Play again", command=self.upload_board)
            play_again_button.grid(row=12, column=0, columnspan=2)
        else:
            if self.human_turn is False:
                self.prepare_move(None, None, symbol)
