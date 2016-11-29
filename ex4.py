__author__ = 'student'

import turtle
turtle.speed(20)
def minkovsky(l, n):
    turtle.shape('turtle')
    assert n >= 0
    if n == 0:
        turtle.forward(l)
        return

    for i in range(n):
        minkovsky(l/4, n-1)
        turtle.left(90)
        minkovsky(l/4, n-1)
        turtle.right(90)
        minkovsky(l/4, n-1)
        turtle.right(90)
        minkovsky(l/4, n-1)
        minkovsky(l/4, n-1)
        turtle.left(90)
        minkovsky(l/4, n-1)
        turtle.left(90)
        minkovsky(l/4, n-1)
        turtle.right(90)
        minkovsky(l/4, n-1)


l = 2000
n = int(input())
minkovsky(l, n)
turtle.mainloop()