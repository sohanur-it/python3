#!/usr/bin/python3

import turtle

turtle.speed(1)

for i in range(10):
	turtle.forward(20)
	turtle.penup()
	turtle.forward(5)
	turtle.pendown()

turtle.exitonclick()

