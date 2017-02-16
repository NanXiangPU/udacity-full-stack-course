import turtle


def draw_square(someTurtle):
    for i in range(4):
        someTurtle.forward(100)
        someTurtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color("yellow")
    pen.speed(3)

    draw_square(pen)

    pen.shape("arrow")
    pen.color("yellow")
    pen.circle(100)

    window.exitonclick()

draw_art()
