import turtle


def draw_square(someTurtle):
    for i in range(4):
        someTurtle.forward(100)
        someTurtle.right(90)


def draw_multiple_squares():
    window = turtle.Screen()
    window.bgcolor("red")

    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(4)
    pen.color("yellow")

    for i in range(36):
        draw_square(pen)
        pen.right(10)

    window.exitonclick()

draw_multiple_squares()