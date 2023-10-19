from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("Purple")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score > self.score
        self.score = 0

    
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGMENT, font=FONT)
    
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGMENT, font=FONT)