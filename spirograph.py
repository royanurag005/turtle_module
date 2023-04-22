import turtle
import turtle as t
import random
radius=100
screen=t.Screen()
timmy=t.Turtle()
angle=0
turtle.colormode(255)
def colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        random_color = colour()
        timmy.color(random_color)
        timmy.circle(radius)
        timmy.setheading(timmy.heading()+size_of_gap)
        timmy.speed(0)
        # angle += 10
# while angle<=360:
#     random_color=colour()
#     timmy.color(random_color)
#     timmy.circle(radius)
#     angle+=10
#
#     print(timmy.heading())
#     timmy.setheading(angle)
#     timmy.speed(10)
draw_spirograph(5)
screen.exitonclick()
