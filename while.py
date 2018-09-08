#!/usr/bin/python3

while True:
	n=input("enter an integer number :")
	n=int(n)

	if n<0:
		print("we only allows positive number,please try again letter :")


	if n==0:
		break
	print("square of",n, "is =" ,n*n)