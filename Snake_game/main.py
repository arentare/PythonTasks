import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#   Screen Settings
screen = Screen()
screen.setup(width=560, height=560)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake")
sleep_time = 0.1
score = 0

is_game = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()
while is_game:
    time.sleep(sleep_time)
    screen.update()
    snake.move()


    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increasescore()
        snake.extend()

    #   Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game = False
        scoreboard.gameover()

    # detection for collision with the tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game = False
            scoreboard.gameover()



screen.exitonclick()
