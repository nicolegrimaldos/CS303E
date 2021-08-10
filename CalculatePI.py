# File: CalculatePI.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/20/20
# Date Last Modified: 10/20/20
# Description of Program: Calculate Pi using a randomly generated number "coordinates"
# program will compute Pi with the random numbers and a specified number of throws. Main function
# will also calculate the difference between the calculated Pi and math.pi

import math
import random


def computePI( numThrows ):
    inside = 0
    for i in range(numThrows):
        positionX = random.uniform(-1.0, 1.0)
        positionY = random.uniform(-1.0, 1.0)
        distance = math.hypot(positionX, positionY)
        if distance < 1:
            inside += 1
    pi = 4 * (inside / numThrows)
    return pi


def main():
    print("Computation of PI using Random Numbers ", '\n')
    n = 100
    while n != 10000000:
        pi_value = computePI(n)
        difference = pi_value - math.pi
        print("num =", format(n, "<9"), end=' ')
        print("Calculated PI =", format(pi_value, "<11.6f"), end='')
        if difference > 0:
            print("Difference =", format(difference, "<+10.6f"))
        else:
            print("Difference =", format(difference, "<-10.6f"))
        n = n * 10
    print("\nDifference = Calculated PI - math.pi")

main()
