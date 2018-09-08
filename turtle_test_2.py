#!/usr/bin/python3

import turtle

turtle.color("blue")
turtle.speed(2)

width=5
turtle.penup()
for x in range(width):
	turtle.dot()
	turtle.forward(20)
	turtle.backward(20*width)
turtle.right(90)

	
turtle.exitonclick()