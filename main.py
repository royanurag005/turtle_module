from turtle import Turtle,Screen
import heroes
tim=Turtle()
tim.shape("turtle")
tim.color("MediumBlue")
for turns in range(4):
    tim.forward(100)
    tim.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)

screen=Screen()
screen.exitonclick()
print(heroes.gen())
