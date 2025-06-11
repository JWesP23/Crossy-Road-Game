import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 30

from turtle import Turtle

class CarManager:

    def __init__(self):
        self.cars = []

    def spawn_cars(self, max_cars):
        #delete all off-screen cars
        while len(self.cars) != 0 and self.cars[0].xcor() < -315:
            self.cars[0].hideturtle()
            del self.cars[0]

        if len(self.cars) < max_cars:
            self.spawn_new_car(random.randrange(-240,241,MOVE_INCREMENT))

    def spawn_new_car(self, yposition):
        new_car = turtle.Turtle(shape= "square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        #cars are 40 x 20 pixels
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.goto(315,yposition)
        overlap = True
        while overlap:
            overlap = False
            for car in self.cars:
                if car.ycor() == yposition and abs(new_car.xcor() - car.xcor()) < 41:
                    overlap = True
                    new_car.setx(new_car.xcor() + 40)
                    break

        self.cars.append(new_car)

    def move_cars(self, additional_speed):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + additional_speed)

    def contact(self, arg):
        for car in self.cars:
            if abs(car.ycor() - arg.ycor()) < 10 and car.distance(arg) < 30:
                return True