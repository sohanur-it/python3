#!/usr/bin/python3


year=input("enter a  year : ")
year=int(year)

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 ==0:
			print(year,"is leap year")
		else:
			print(year,"is not leap year")
	else:
		print(year,"is leap year")
else:
	print(year, "is not leap year")
