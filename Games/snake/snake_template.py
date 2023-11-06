from tkinter import *
import random
import logging

logging.basicConfig(level='DEBUG', format='%(levelname)s - %(message)s')

GAME_WIDTH  = 1200                        # x-Achse
GAME_HEIGHT = 700                         # y-Achse
SPEED = 100
SPACE_SIZE = 50                            # ein Quadrat im Feld
SNAKE_COLOR = "#00FF00"

BG_COLOR    = "#000000"

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


# SPIEL CODES:

# 1. Spielbeginn programmieren

def new_game():                  # Funktion neues Spiel mit Leertaste starten
    
    global end_screen
    
    if end_screen:
        logging.info("Neues Spiel gestartet!")
        
        end_screen = False        # so bleibt er beim Spiel


        canvas.delete(ALL)       # Spielfeld löschen


        snake = Snake()          # Klasse Snake
        

# 2. Schlange programmieren mit einer Klasse

class Snake:
    
    def __init__(self):
        self.coordinates = [(0, 0), (0, 0), (0, 0)]            # wo erscheint Schlange - Koordinaten
        self.squares = []
        
        
        # Schlange malen mit canvas.modul
        for x, y in self.coordinates:                          
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            
        














window = Tk()
window.title("Snake Game")
window.resizable(False, False)

end_screen = True

label = Label(window, text="Score:{}".format(0), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<space>', lambda event: new_game())    

window.mainloop()