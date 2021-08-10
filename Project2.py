# File: Project2.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/31/20
# Date Last Modified: 11/02/20
# Description of Program: Building a Prime Factorization Factory where the user can either factor, find is the
# input is prime, and end.

import math


def isPrime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        if num == 2:
            return True
        else:
            return False
    divisor = 3
    while divisor <= math.sqrt(num):
        if num % divisor == 0:
            return False
        else:
            divisor += 2
    return True


def findNextPrime(num):
    if num < 2:
        return 2
    if num % 2 == 0:
        num -= 1
    guess = num + 2
    while not isPrime(guess):
        guess += 2
    return guess


def factor(num):
    original_num = num
    if isPrime(num):
        factor_list = [num]
        print("The prime factorization of", num, "is:", factor_list, "\n")
    else:
        factor_list = []
        d = int(2)
        while num > 1:
            if num % d == 0:
                factor_list.append(d)
                num /= d
            else:
                d = findNextPrime(d)
        print("The prime factorization of", original_num, "is:", factor_list, "\n")


def factory():
    print("Welcome to the Prime factory!\n")
    command = input("Enter a command (factor, isprime, end): ")
    command = command.lower()
    while command != "end":
        if command == "factor":
            num = int(input("Enter an integer > 1: "))
            if num > 1:
                factor(num)
            else:
                print("Illegal input: ", num, "; input must be an integer > 1.\n", sep="")
            command = input("Enter a command (factor, isprime, end): ")
            command = command.lower()
        elif command == "isprime":
            num = int(input("Enter an integer > 1: "))
            if num < 2:
                print("Illegal input: ", num, "; input must be an integer > 1.\n", sep="")
            else:
                if isPrime(num):
                    print("The number", num, "is prime\n")
                elif not isPrime(num):
                    print("The number", num, "is not prime\n")
            command = input("Enter a command (factor, isprime, end): ")
            command = command.lower()
        else:
            print("Command", command, "not recognized. Try again!\n")
            command = input("Enter a command (factor, isprime, end): ")
            command = command.lower()
    print("Thanks for using out service! Goodbye.", end="")


factory()
