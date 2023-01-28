import math


a = int(input("enter length of side 1"'\n'))
b = int(input("enter length of side 2"'\n'))
c = int(input("enter length of side 3 "'\n'))
s = (a+b+c)/2

print("area is ",(math.sqrt(s*(s-a)*(s-b)*(s-c))))