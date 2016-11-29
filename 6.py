import turtle
turtle.speed(20)


def reverse_c(c):
    reversed_c = []
    for i in range(0, len(c)):
        reversed_c.append(c[len(c) - i - 1])
    return reversed_c

def transform_c(c):

    transformed_c = []
    for item in c:
        if item == "L":
            transformed_c.append("U")
        elif item == "R":
            transformed_c.append("D")
        elif item == "U":
            transformed_c.append("R")
        elif item == "D":
            transformed_c.append("L")
    return transformed_c

def dragon_c(c, n):

    for i in range(n):
        c += transform_c(reverse_c(c))
    return c


def draw_c(c, linewidth):
    for item in c:
        if item == "R":
            turtle.setheading(0)
        elif item == "U":
            turtle.setheading(90)
        elif item == "L":
            turtle.setheading(180)
        elif item == "D":
            turtle.setheading(270)
        turtle.forward(linewidth)
    turtle.exitonclick()

c = ["L", "U"]
n = int(input())
l = 2**(n+1)


if n <= 8:
    linewidth = 10
elif n <= 11:
    linewidth = 5
else:
    linewidth = 2


d_c = dragon_c(c, n)
draw_c(d_c, linewidth)