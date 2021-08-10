# File: DaysInMonth.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 09/16/2020
# Date Last Modified: 09/16/2020
# Description of Program: Ask the user to enter the month and year and display the correct number
# of days in that month, also accounting for leap years.

import calendar


def main():
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    if month == 4 or month == 6 or month == 11:
        days = 30
    elif month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    days = 29
                else:
                    days = 28
            else:
                days = 29
        else:
            days = 28
    else:
        days = 31
    print(calendar.month_name[month], year, "has", days, "days")


main()
