import turtle as t
import random

# Assignments for random walk
jim = t.Turtle("turtle")
t.colormode(255)
jim.pensize(5)
jim.speed("fast")
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
    jim.color(color_set)
    jim.forward(distance)
    jim.setheading(random.choice(directions_set))


# Draw a random wolk with random color
for i in range(200):
    random_walk(random_color(), directions, 30)

tim = t.Turtle("circle")
tim.speed("fast")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        jim.color(random_color())
        jim.circle(10)
        jim.setheading(tim.heading() + size_of_gap)


# draw_spirograph(25)

screen = t.Screen()
screen.exitonclick()
