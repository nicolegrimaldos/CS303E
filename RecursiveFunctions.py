# File: RecursiveFunctions.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/11/2020
# Date Last Modified: 11/20/2020
# Description of Program: Practicing using recursive functions on problems
# or concepts solved earlier in the semester without recursive functions.


def sumItemsInList(L):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList(L[1:])


def countOccurrencesInList(key, L):
    """ Return the number of times key occurs in
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList(key, L[1:])
    else:
        return countOccurrencesInList(key, L[1:])


def addToN(n):
    """ Add up the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
    if n <= 1:
        return 0
    else:
        return n + addToN(n - 1)


def findSumOfDigits(n):
    """ Return the sum of the digits in a non-negative integer. """
    if n <= 0:
        return 0
    else:
        return n % 10 + findSumOfDigits(n // 10)


def decimalToBinary(n):
    """ Given a nonnegative decimal n, return the
      binary representation as a string. """
    if n < 2:
        if n == 0:
            return 0
        else:
            return 1
    return str(decimalToBinary(n // 2)) + str(n % 2)


def decimalToList(n):
    """ Given a positive decimal integer, return a list of the
   digits (as strings). """
    n = int(n)
    if n > 0:
        return decimalToList(n / 10) + [str(n % 10)]
    else:
        return []


def isPalindrome(s):
    """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """
    if s == '':
        return True
    elif s[0] == s[len(s) - 1]:
        return isPalindrome(s[1:len(s) - 1])
    else:
        return False


def findFirstUppercase(s):
    """ Return the first uppercase letter in
   string s, if any.  Return None if there
   is none. """
    if s == "":
        return None
    elif 65 <= ord(s[0]) < 91:
        return s[0]
    else:
        return findFirstUppercase(s[1:])


def findFirstUppercaseIndexHelper(s, index):
    """ Helper function for findFirstUppercaseIndex. """
    if s == "":
        return -1
    elif 65 <= ord(s[0]) < 91:
        return index
    else:
        index += 1
        return findFirstUppercaseIndexHelper(s[1:], index)


# The following function is already completed for you.  But
# make sure you understand what it's doing.

def findFirstUppercaseIndex(s):
    """ Return the index of the first uppercase letter in
   string s, if any.  Return -1 if there is none.  This one
   requires a helper function, which is the recursive
   function. """
    return findFirstUppercaseIndexHelper(s, 0)
