from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        # self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-260, 260) // 20 * 20
        y = random.randint(-260, 260) // 20 * 20
        self.goto(x, y)
