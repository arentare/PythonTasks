from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.write(f"Score: {self.score}", False, ALIGNMENT, font=FONT)

    def increasescore(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
