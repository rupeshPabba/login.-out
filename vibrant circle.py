from ast import While
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
a=0
b=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.backward(a)
    t.left(b)
    a+=4
    b+=1
    if b==210:
        break
    turtle.hideturtle()

turtle.done()