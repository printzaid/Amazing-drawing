# Python program to draw
# Rainbow Benzene
# using Turtle Programming
# Made with love
import turtle
colors = ['white', 'grey', 'white', 'grey', 'white', 'grey']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
