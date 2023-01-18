# from turtle import Turtle, Screen
# import random

# t = Turtle()
#
# #t.shape("turtle")
# #t.fillcolor("red")
#
# # for i in range(4):
# #     t.forward(100)
# #     t.right(90)
#
#
# # for i in range(10):
# #     t.forward(10)
# #     t.penup()
# #     t.forward(10)
# #     t.pendown()
# screen = Screen()
# screen.colormode(255)
#
# for i in range (3, 11):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     # print(r)
#
#     t.pencolor(r, g, b)
#
#     for x in range(i):
#         t.forward(100)
#         t.right(360/i)
#
# #
# #
#
# screen.exitonclick()

# ----------------------
## RANDOM WALK ##

from turtle import Turtle, Screen
import random

t = Turtle()

screen = Screen()
screen.colormode(255)

distance = 100
direction = [0, 90, 180, 270]
t.width(10)

for i in range (1, distance):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    t.pencolor(r, g, b)

    t.forward(20)
    t.setheading(random.choice(direction))




screen.exitonclick()
