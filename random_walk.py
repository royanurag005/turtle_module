import random
import turtle
timmy=turtle.Turtle()
# color=["white","white smoke","gainsboro","light gray","black","dark green",
#        "medium blue","lime","red","dark slate blue","indigo","gold",
#        "light salmon","green"]
turtle.colormode(255)
def color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colour=(r,g,b)
    return colour
timmy.width(10)
angle=[0,90,180,270]
screen=turtle.Screen()
timmy.speed(10)
for round in range(0,500):
    timmy.color(color())
    timmy.forward(20)
    timmy.setheading(random.choice(angle))

screen.exitonclick()
