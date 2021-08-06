import turtle
import random

from turtle import Turtle, Screen
screen = Screen()
screen.setup(500, 400)
colors = ["red", "orange", 'yellow', "green", "blue", "purple"]
all_turtles = []
y = -75
is_race_on = False
for index in range(len(colors)):
    col = colors[index]
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(col)
    new_turtle.goto(-230, y)
    y += 30
    all_turtles.append(new_turtle)



# red = Turtle("turtle")
# red.penup()
# red.color("red")



dasha_bet = screen.textinput("Dasha, make your bet", "Dasha, which cherepashka win the race?: ")
zhenya_bet = screen.textinput("Zhenya, make your bet", "Zhenya, which cherepashka win the race?: ")

if dasha_bet and zhenya_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance )
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == dasha_bet:
                print("DASHA WINS!")
            elif winning_color == zhenya_bet:
                print("ZHENYA WINS!")
            else:
                print("Nobody won. Please try again.   ")




# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def move_right():
#     tim.right(10)
# def move_left():
#     tim.left(10)
#
# def clean():
#     turtle.resetscreen()
#
# screen.listen()
#
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(move_right, "d")
# screen.onkey(move_left, "a")
# screen.onkey(clean, "c")
screen.exitonclick()