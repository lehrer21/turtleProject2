# A simple app recreating an etch-a-sketch using the Turtle module.
from turtle import Turtle, Screen


my_turtle = Turtle()
screen = Screen()


def move_forwards():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.backward(10)


def turn_right():
    my_turtle.right(10)


def turn_left():
    my_turtle.left(10)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()