# File: MyStringFunctions.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/26/20
# Date Last Modified: 10/26/20
# Description of Program: Building a string library, a collection of functions on strings

def myAppend( str , ch ):
    # Return a new string that is like str but with
    # character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    num = 0
    for i in str:
        if ch == i:
            num +=1
    return num

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2 in order.
    return str1 + str2

def myMin(str):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    lowest = 127
    empty = "Yes"
    for i in str:
        character = ord(i)
        if character < lowest:
            lowest = character
            empty = "No"
    if empty == "Yes":
        print("Empty string: no min value")
        return None
    else:
        lowest = chr(lowest)
        print(lowest)

def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    length = 0
    new_string = ""
    if length == i:
        new_string = ch + str
    else:
        if i > len(str):
            print("Invalid index")
            return None
        else:
            for x in str:
                if length < i:
                    new_string += x
                    length += 1
                elif length == i:
                    new_string += ch + x
                    length += 1
                elif length > i:
                    new_string += x
                    length += 1
    return new_string

def myPop(str, i):
    # Return two results:
    # 1. a new string that is like str but with the ith
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or
    # equal to len(str), and return str unchanged and None
    length = 0
    new_string = ""
    removed = 0
    if i >= len(str):
        print("Invalid index")
        return str, None
    else:
        for x in str:
            if length < i:
                new_string += x
                length += 1
            elif length == i:
                removed = x
                length += 1
            elif length > i:
                new_string += x
                length += 1
        return new_string, removed

def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    index = ""
    i = 0
    found = "No"
    for x in str:
        if ch == x:
            found = "Yes"
            index = i
        elif found == "No":
            i += 1
    if found == "No":
        return -1
    else:
        return index

def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    index = ""
    i = 0
    found = "No"
    for x in str:
        if ch == x:
            found = "Yes"
            index = i
            i += 1
        else:
            i += 1
    if found == "No":
        return -1
    else:
        return index

def myRemove(str, ch):
    # Return a new string with the first occurrence of ch
    # removed.  If there is none, return str.
    new_string = ""
    found = "No"
    for x in str:
        if x != ch or found == "Yes":
            new_string += x
        elif x == ch and found == "No":
            found = "Yes"
    if found == "Yes":
        return new_string
    else:
        return str

def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    new_string = ""
    found = "No"
    for x in str:
        if x != ch:
            new_string += x
        elif x == ch:
            found = "Yes"
    if found == "Yes":
        return new_string
    else:
        return str

def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order.
    new_string = ""
    for x in str:
        new_string = x + new_string
    return new_string

