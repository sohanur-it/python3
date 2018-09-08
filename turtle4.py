#!/usr/bin/python3

import turtle

turtle.speed(1)
for side_length in range(50, 130 , 10):
	for i in range(3):
		turtle.forward(side_length)
		turtle.left(120)
turtle.exitonclick()