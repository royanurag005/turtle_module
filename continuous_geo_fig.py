import turtle as t
import random
tim = t.Turtle()
color=["white","white smoke","gainsboro","light gray","black","dark green",
       "medium blue","lime","red","dark slate blue","indigo","gold","light sky blue"
       "light salmon","green"]
########### Challenge 3 - Draw Shapes ########
for figure in range(3,11):
    angle=360/figure
    colour=random.choice(color)
    # colour=t.pencolor(r, g, b)
    for sides in range(figure):
        tim.color(colour)
        tim.forward(100)
        tim.right(360-angle)

screen=t.Screen()
screen.exitonclick()
