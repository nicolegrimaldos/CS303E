# File: EasterSunday.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 9/04/20
# Date Last Modified: 9/04/20
# Description of Program: This program computes the date of Easter
# Sunday for a specified year given from the user

y = int(input("Enter year: "))
a = y % 19
b = int(y/100)
c = y % 100
d = int(b/4)
e = b % 4
g = int((8 * b + 13)/25)
h = int((19*a+b-d-g+15)%30)
j = int(c/4)
k = c % 4
m = int((a+11*h)/319)
r = ((2*e+2*j-k-h+m+32)%7)
n = int((h-m+r+90)/25)
p = ((h-m+r+n+19)%32)

print("In 2001 Easter Sunday is on month", n, "and day",p)


