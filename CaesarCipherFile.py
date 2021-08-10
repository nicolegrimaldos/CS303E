# File: CaesarCipherFile
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/05/20
# Date Last Modified: 11/05/20
# Description of Program: User will either want to decrypt or encrypt a file
# the user will also input a shift value. The user will name a file to decrypt or encrypt
# the program will write a file FILENAME-Enc or FILENAME-Dec with the appropriate text.


import os.path


def decrypt(text, shiftValue):
    new_phrase = ""
    for ch in text:
        if ch == " ":  # append spaces
            new_phrase += " "
        else:
            if 65 <= ord(ch) < 91:  # append uppercase
                W = ord(ch) - ord("A")
                X = (W + shiftValue) % 26
                Y = X + ord("A")
                Z = chr(Y)
                new_phrase += Z
            elif 97 <= ord(ch) < 123:  # append lowercase
                W = ord(ch) - ord("a")
                X = (W + shiftValue) % 26
                Y = X + ord("a")
                Z = chr(Y)
                new_phrase += Z
            else:
                new_phrase += ch  # append non letter characters
    return new_phrase


def encrypt(text, shiftValue):
    new_phrase = ""
    for ch in text:  # append spaces
        if ch == " ":
            new_phrase += " "
        else:
            if 65 <= ord(ch) < 91:  # append uppercase
                W = ord(ch) - ord("A")
                X = (W + shiftValue) % 26
                Y = X + ord("A")
                Z = chr(Y)
                new_phrase += Z
            elif 97 <= ord(ch) < 123:  # append lowercase
                W = ord(ch) - ord("a")
                X = (W + shiftValue) % 26
                Y = X + ord("a")
                Z = chr(Y)
                new_phrase += Z
            else:
                new_phrase += ch
    return new_phrase


def main():
    command = input("Enter Caesar cipher command (encrypt/decrypt): ")
    formatted_command = command.lower()
    if formatted_command == "encrypt":
        print("You’ve asked to encrypt.")
        shiftValue = int(input("Please enter shift value (0 .. 25): "))
        if 0 <= shiftValue < 26:
            name = input("Please enter filename with text to encrypt: ")
            if not os.path.isfile(name):
                print("File does not exist")
                return
            new_name = name + "-Enc"
            print("The input filename is", name)
            print("The output filename is", new_name)
        else:
            print("Illegal shift value:", shiftValue)

    if formatted_command == "decrypt":
        print("You’ve asked to decrypt.")
        shiftValue = int(input("Please enter shift value (0 .. 25): "))
        if 0 <= shiftValue < 26:
            name = input("Please enter filename with text to decrypt: ")
            if not os.path.isfile(name):
                print("File does not exist")
                return
            shiftValue = (26 - shiftValue)
            new_name = name + "-Dec"
            print("The input filename is", name)
            print("The output filename is", new_name)
        else:
            print("Illegal shift value:", shiftValue)

    infile = open(name, "r")
    outfile = open(new_name, "w")
    for line in infile:
        if command == "decrypt":
            new_line = decrypt(line, shiftValue)
        elif command == "encrypt":
            new_line = encrypt(line, shiftValue)
        outfile.write(new_line)

    infile.close()
    outfile.close()


main()
