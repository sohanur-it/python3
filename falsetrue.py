#!/usr/bin/python3

saarc=['bangladesh','pakisthan','india','srilanka','nepal','maldip','bhutan']
print(saarc)
print(saarc[0])
print(saarc[6])
print("bangladesh" in saarc)
print("china" in saarc)
print(len(saarc))

country=input("what is your country name ? ")
if country in saarc:
	print(country,"is a member of saarc")
else:
	print(country,"is not a member of saarc")
print("program terminated")