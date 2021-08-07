from turtle import Screen, Turtle

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




# New Paddle created

turtle = Turtle()
turtle.speed(0)
turtle.penup()
turtle.shape("square")
turtle.color("white")
turtle.turtlesize(stretch_wid=5, stretch_len=1)
turtle.goto(350, 0)

















screen.exitonclick()
