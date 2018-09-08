#!/usr/bin/python3


import turtle

height=10
width=7 

turtle.color("orange")

turtle.speed(2)

turtle.penup()

for y in range(height):
	for x in range(width):
		turtle.dot()
		turtle.forward(20)
	turtle.backward(20*width)
	turtle.right(90)
	turtle.forward(20)
	turtle.left(90)

turtle.exitonclick()