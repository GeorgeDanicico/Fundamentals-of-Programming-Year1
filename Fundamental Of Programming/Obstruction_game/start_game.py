from jproperties import Properties

from UI.Console import Console_UI
from UI.GUI import GUI

settings_data = Properties()

with open('settings.properties', 'rb') as files:
    settings_data.load(files)

UI_mode = settings_data.get("game_mode").data
UI_mode = UI_mode[1:-1]

if UI_mode == "console":
    game = Console_UI()
    game.start()
elif UI_mode == "gui":
    game = GUI()
