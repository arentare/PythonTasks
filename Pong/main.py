from turtle import Screen, Turtle
from paddle import Paddle

#   Parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
DIV_COLOR = "white"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)

divider = Turtle()
divider.speed(0)
divider.penup()
divider.pencolor(DIV_COLOR)
divider.sety(SCREEN_WIDTH)
divider.setheading(270)
divider.pendown()
divider.forward(800 * 2)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


screen.exitonclick()