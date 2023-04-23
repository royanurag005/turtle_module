# import colorgram
# colors=colorgram.extract("image_hirst.jpg",10)
# list=[]
# # for items in colors:
# #     list_colors.append(items.rgb)
# # print(list_colors)
#
# #Desired format
# for items in colors:
#     r=items.rgb.r
#     g=items.rgb.g
#     b=items.rgb.b
#     color=(r,g,b)
#     list.append(color)
# print(list_colors)
import turtle

list_colours=[(197, 162, 110), (132, 165, 191), (240, 225, 233), (224, 238, 231), (71, 97, 133), (149, 88, 59), (136, 69, 93), (184, 146, 165)]
from turtle import Screen, Turtle
import random
timmy=Turtle()
screen=Screen()
timmy.penup()
timmy.speed(0)
ini_x=-200
ini_y=-200
timmy.setx(ini_x)
timmy.sety(ini_y)
turtle.colormode(255)
for _ in range(10):
    for char in range(10):
        color=random.choice(list_colours)
        timmy.pendown()
        timmy.dot(20,color)
        timmy.penup()
        timmy.forward(50)
    ini_x=-200
    ini_y+=50
    timmy.setx(ini_x)
    timmy.sety(ini_y)
timmy.hideturtle()
screen.exitonclick()
