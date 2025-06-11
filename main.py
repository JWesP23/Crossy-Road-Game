import time
from turtle import Screen, Turtle

import scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def set_lines():
    line_drawer = Turtle(visible= False)
    line_drawer.penup()
    line_drawer.color("white")
    line_drawer.setheading(180)
    line_drawer.goto(315,255)
    line_drawer.pendown()
    line_drawer.goto(-315,255)
    line_drawer.penup()
    line_drawer.goto(315,-255)
    line_drawer.pendown()
    line_drawer.goto(-315,-255)
    for i in range(-225, 251, 30):
        line_drawer.penup()
        line_drawer.goto(315,i)
        for j in range(0, 31):
            line_drawer.pendown()
            line_drawer.forward(10)
            line_drawer.penup()
            line_drawer.forward(10)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

set_lines()

player_turtle = Player()
car_manager = CarManager()
level_counter = Scoreboard("Level:", (-220,255), "white", True)

level = 0
screen.listen()
game_is_on = True
loop_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if loop_counter % 6 == 0:
        loop_counter = 0
        if level < 50:
            car_manager.spawn_cars(10 + 3 * level)
            car_manager.move_cars(level)
        else:
            car_manager.spawn_cars(160)
            car_manager.move_cars(50)

    screen.onkeypress(key= "w", fun= player_turtle.move_forward)
    screen.onkeypress(key= "Up", fun= player_turtle.move_forward)
    screen.onkeypress(key= "d", fun= player_turtle.move_right)
    screen.onkeypress(key= "Right", fun= player_turtle.move_right)
    screen.onkeypress(key= "a", fun= player_turtle.move_left)
    screen.onkeypress(key= "Left", fun= player_turtle.move_left)
    screen.onkeypress(key= "s", fun= player_turtle.move_down)
    screen.onkeypress(key= "Down", fun= player_turtle.move_down)

    if player_turtle.check_level_up():
        level += 1
        level_counter.append_level(1)

    if car_manager.contact(player_turtle):
        game_is_on = False

screen.update()
game_over = scoreboard.Scoreboard("Game Over", (0,10), "white", False)
screen.exitonclick()