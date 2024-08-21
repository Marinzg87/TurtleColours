import turtle as t
import random

tim = t.Turtle("turtle")
t.colormode(255)
tim.pensize(5)
tim.speed("fast")
directions = [0, 90, 180, 270]


def random_color():
    """Return tuple with random RGB values"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_set = (r, g, b)
    return color_set


def random_walk(color_set, directions_set, distance):
    """Return random walk"""
    tim.color(color_set)
    tim.forward(distance)
    tim.setheading(random.choice(directions_set))


for i in range(200):
    random_walk(random_color(), directions, 30)

screen = t.Screen()
screen.exitonclick()
