__author__ = 'student'

import turtle
turtle.speed(20)
def koch(l, n):
    assert n >= 0
    assert l >= 0
    turtle.shape('turtle')
    if n == 0:
        turtle.forward(l)
        return

    for i in range(n):
        koch(l/3, n-1)
        turtle.left(60)
        koch(l/3, n-1)
        turtle.right(120)
        koch(l/3, n-1)
        turtle.left(60)
        koch(l/3, n-1)
        return

def snowflake(l, n):
    assert n >= 0
    assert l >= 0
    koch(l, n)
    turtle.right(120)
    koch(l, n)
    turtle.right(120)
    koch(l, n)
    turtle.right(120)
    return





l = 200
n = int(input())
snowflake(l, n)
turtle.mainloop()

