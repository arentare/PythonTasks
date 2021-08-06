import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# i = 3
# while True:
#     degree = 360 / i
#     for a in range(i):
#         tim.forward(10)
#         tim.right(degree)
#     i += 1
#
# screen = Screen()
# screen.exitonclick()

turtle.colormode(255)

def random_color():
    random_red = random.randint(0,255)
    random_green = random.randint(0,255)
    random_blue = random.randint(0,255)
    return((random_red, random_green, random_blue))

moves = [0, 90, 180, 270]
tim.speed(0)
# tim.pensize(5)

# while True:
#     tim.forward(50)
#
#     tim.seth(random.choice(moves))
#     tim.pencolor(random_color())
size = 100
change_size = [1, -1]

for _ in range (360):
    tim.circle(size)
    tim.left(1)
    tim.pencolor(random_color())
    size += 1

screen = Screen()
screen.exitonclick()