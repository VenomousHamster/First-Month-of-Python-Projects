from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.list_of_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_num = random.randint(1, 6)
        if random_num == 6:
         car = Turtle("square")
         car.penup()
         car.shapesize(1,2)
         car.color(random.choice(COLORS))
         random_y = random.randint(-200,200)
         car.goto(280,random_y)
         self.list_of_cars.append(car)

    def move_cars(self):
        for i in range(len(self.list_of_cars)):
            self.list_of_cars[i].backward(self.car_speed)

    def speed_increase(self):
       self.car_speed += MOVE_INCREMENT
