from Board.board import Board
from Console.UI import UI
from Game.game_service import Game
from Settings import Settings

settings = Settings("settings.properties")
dimension = 0
number_of_apples = 0
try:
    dimension = int(settings.get_dimension)
    number_of_apples = int(settings.get_apples)
    if number_of_apples + 3 >= dimension ** 2:
        raise Exception("Too many apples! The snake can't eat all of them!...\n")

except Exception as ve:
    print(str(ve))
    exit(0)

board = Board(dimension, number_of_apples)
game = Game(board)
ui = UI(game)
ui.start()