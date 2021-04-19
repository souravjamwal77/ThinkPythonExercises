import turtle

bob = turtle.Turtle()

print(bob)

def square(t, length):
    """Draws a square using turtle object.

    Args:
        t (Turtle Object): A turtle object to draw a Square.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)



def polygon(t, length, n):
    """Draws a polygon with given n sides, with each side of given length.

    Args:
        t (Turtle Object): A turtle object for drawing the given shape.
        length (px): length of the each side
        n (int): number of sides
    """
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)



def circle(t, r):
    """Draws a circle using Turtle object with radius r.

    Args:
        t (Turtle Object): A turtle object to draw required shape.
        r (int): radius of the circle
    """
    circumference = r * 3.1415
    




turtle.mainloop()