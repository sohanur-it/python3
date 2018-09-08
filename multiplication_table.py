#!/usr/bin/python3

n=input("enter a integer number : ")
n=int(n)
print("using while loop")
m=1
while m<=10:
	print(n,"*",m,"=",n*m)
	m+=1
print("using for loop")

for m in range(1,10):
	print(n,"*",m,"=",n*m)
	m+=1