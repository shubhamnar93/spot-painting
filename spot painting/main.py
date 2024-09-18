import random
import turtle as t
from colour import ColorExtractor

m = ColorExtractor()
rgb_color = m.extract_colors()

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
tim.penup()
tim.ht()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
amount_dots=100

for dot in range(1, amount_dots+1):
    tim.dot(20, random.choice(rgb_color))
    tim.fd(50)

    if dot %10==0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=t.Screen()
screen.exitonclick()