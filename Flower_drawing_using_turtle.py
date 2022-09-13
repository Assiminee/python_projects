""" Draws a flower using turtle """

import math
import turtle
from turtle import *
radius = int(input("What is the radius of the flower? "))
petals = int(input("How many petals do you want? "))


def draw_arc(b,r):
    c = 2*math.pi*r #Circumference of circle
    ca = c/(360/60)  #Circumference of arc (assume 60 degree central angle of sector as above)
    n = int(ca/3)+1  #number of segments
    l = ca/n  #length of segment
    for i in range(n):
        b.fd(l)
        b.lt(360/(n*6))


def draw_petal(b,r):
    speed(35)
    draw_arc(b,r)
    b.lt(180-60)
    draw_arc(b,r)


bob = turtle.Turtle()


for i in range(petals):
    draw_petal(bob,radius)
    bob.lt(360/petals)

turtle.mainloop()
