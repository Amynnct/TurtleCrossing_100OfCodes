from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(-270, 250)
        self.hideturtle()
        self.level = 0
        self.update_level()
    
    def update_level(self):
        self.clear()
        self.write("Level: {}".format(self.level),font=FONT)

    def level_up(self):
        self.level += 1 
        self.update_level()
    
    def game_over(self):
        self.goto(-90,0)
        self.write("GAME OVER!",font=FONT)
