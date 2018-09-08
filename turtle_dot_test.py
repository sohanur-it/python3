#!/usr/bin/python3

import turtle

turtle.color("blue")
turtle.speed(2)

turtle.penup()
for i in range(4):
	for x in range(5):
		turtle.dot()
		turtle.forward(20)
	turtle.right(90)

	
turtle.exitonclick()