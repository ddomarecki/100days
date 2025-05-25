from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
tim.color("green")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
screen = Screen()
# screen.exitonclick()


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# screen.exitonclick()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed"]
#
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 /num_sides
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)
#

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed(0 )

for _ in range (200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen.exitonclick()