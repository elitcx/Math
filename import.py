import math2
from turtle import *

setup(1600,900)
screensize(1280,1280)
hideturtle()
penup()
speed(0)
width(10)
left(90)
goto(-700, -350)
percentage = 20

for i in range(5):
    pendown()
    forward(percentage * 35)
    penup()
    left(90)
    forward(30)
    right(90)
    back(10)
    write(f"{percentage}%", align='center', font= ("Arial", 15, "normal"))
    width(3)
   
    forward(10)
    right(90)
    forward(30)
    dash_count = 1
    color('blue')
    for x in range(55):
        if dash_count %2 != 0:
            pendown()
            forward(12.5)
            penup()
        else:
            pass
        forward(12.5)
    color('black')
    left(90)
    width(10)
    goto(-700,-350)
    percentage -= 5


right(90)


for i in range(11):
    pendown()
    forward(125)
    penup()
    right(90)
    forward(50)
    write(math2.strprob[i], align='center', font= ("Arial", 15, "normal"))
    back(50)
    left(180)
    pendown()
    color('red')
    width(20)
    forward((math2.probabilities[i] * 35))
    penup()
    forward(5)
    write(f"{math2.probabilities[i]}%", align='center', font= ("Arial", 15, "bold"))
    back(5)
    back((math2.probabilities[i] * 35))
    color('black')
    width(10)
    right(90)
pendown()
right(180)
forward(1375)
penup()


mainloop()