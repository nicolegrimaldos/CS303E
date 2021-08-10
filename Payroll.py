# File: Payroll.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 9/09/2020
# Date Last Modified: 9/14/2020
# Description of Program: Prints a payroll statement based on given information from the user like
#name, number  of hours  worked in a week, hourly rate, federal tax withholding  rate, and  state tax withholding rate.

def main():
    Name = input("Enter employee’s name: ")
    Hours = float(input("Enter number of hours worked in a week: "))
    Rate = float(input("Enter hourly pay rate: "))
    FedRate = float(input("Enter federal tax withholding rate: "))
    StateRate = float(input("Enter state tax withholding rate: "))

    GrossPay = Rate * Hours
    FedWithholding = GrossPay * FedRate
    FedPercentage = FedRate * 100
    StateWithholding = GrossPay * StateRate
    StatePercentage = StateRate * 100
    TotalDeduction = FedWithholding + StateWithholding
    NetPay = GrossPay - TotalDeduction

    print("")
    print("Employee Name:",Name)
    print("Hours Worked:",Hours)
    print("Pay Rate: $", Rate, sep='')
    print("Gross Pay: $","%.2f" % GrossPay, sep='')
    print("Deductions:")
    print("  Federal Withholding (", FedPercentage, "%): $", "%.2f" % FedWithholding, sep='')
    print("  State Withholding (", StatePercentage, "%): $", "%.2f" % StateWithholding, sep='')
    print("  Total Deduction: $", "%.2f" % TotalDeduction, sep='')
    print("Net Pay: $","%.2f" % NetPay, sep='')

main()








