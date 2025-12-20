import turtle
import time
import random

width, height = 500, 500
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

def get_turtle_number():
    racers = 0
    while True:
        racers = input("Enter the number of racers (1-6): ")
        if racers.isdigit() and 1 <= int(racers) <= 6:
            return int(racers)
        else:
            print("Invalid turtle number.")

def create_turtle(color):
    turtles = []
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setposition(-200, 200 - i * 50)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtle(colors1)
    while True:
        for racer in turtles:
            distance = random.randint(1, 10)
            racer.forward(distance)
            if racer.ycor() >= 200:
                print(f"The winner is the {racer.pencolor()} turtle!")
                return
        


def init_turtle():
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Turtle racing")

racers = get_turtle_number()
init_turtle()
random.shuffle(colors)
colors1 = colors[:racers]
race(colors1)
time.sleep(5)
