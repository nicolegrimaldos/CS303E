# File: MinMax.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 09/21/2020
# Date Last Modified: 09/21/2020
# Description of Program: User will input any number of integers and the program
# will print out the minimum and maximum of the numbers entered



def main():
    Input_Number = input("Enter an integer or 'stop' to end: ")
    Values_Entered = "no"
    nums = []
    while Input_Number != "stop":
        nums.append(int(Input_Number))
        Values_Entered = "yes"
        Input_Number = input("Enter an integer or 'stop' to end: ")
    if Input_Number == "stop":
        if Values_Entered == "no":
            print("You didn't enter any numbers")
        else:
            print("The maximum is", max(nums))
            print("The minimum is", min(nums))
main()

























