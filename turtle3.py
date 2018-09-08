#!/usr/bin/python3

import turtle

turtle.speed(2)
for side_length in range(50, 130 , 20):
	for i in range(4):
		turtle.forward(side_length)
		turtle.left(90)
turtle.exitonclick()