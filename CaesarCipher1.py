# File: CaesarCipher.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 09/22/2020
# Date Last Modified: 09/22/2020
# Description of Program: User will either ask the program to Encrypt or Decrypt using the CaesarCipher
# and the program will print out the encryption or decryption based on the entered shift


def decrypt():
    text_length = len(text)
    new_phrase = ""
    for i in range(text_length):
        letter = text[i]
        if letter == " ":  # append spaces
            new_phrase += " "
        else:
            if 65 <= ord(letter) < 91:  # append uppercase
                W = ord(letter) - ord("A")
                X = (W - shift) % 26
                Y = X + ord("A")
                Z = chr(Y)
                new_phrase += Z
            elif 97 <= ord(letter) < 123:  # append lowercase
                W = ord(letter) - ord("a")
                X = (W - shift) % 26
                Y = X + ord("a")
                Z = chr(Y)
                new_phrase += Z
            else:
                new_phrase += letter  # append non letter characters
    return new_phrase


def encrypt():
    text = input("Please enter text to encrypt: ")
    text_length = len(text)
    new_phrase = []
    for i in range(text_length):  # append spaces
        letter = text[i]
        if letter == " ":
            new_phrase.append(" ")
        else:
            if 65 <= ord(letter) < 91:  # append uppercase
                W = ord(letter) - ord("A")
                X = (W + shift) % 26
                Y = X + ord("A")
                Z = chr(Y)
                new_phrase.append(Z)
            elif 97 <= ord(letter) < 123:  # append lowercase
                W = ord(letter) - ord("a")
                X = (W + shift) % 26
                Y = X + ord("a")
                Z = chr(Y)
                new_phrase.append(Z)
            else:
                new_phrase.append(letter)  # append non letter characters
    print("The encrypted text is:", ''.join(map(str, new_phrase)))


command = input("Enter Caesar cipher command (encrypt/decrypt): ")
formatted_command = command.lower()
if formatted_command == "encrypt":
    print("You’ve asked to encrypt.")
    shift = int(input("Please enter shift value (0 .. 25): "))
    if 0 <= shift < 26:
        encrypt()
    else:
        print("Illegal shift value:", shift)
elif formatted_command == "decrypt":
    print("You’ve asked to decrypt.")
    shift = int(input("Please enter shift value (0 .. 25): "))
    if 0 <= shift < 26:
        decrypt()
    else:
        print("Illegal shift value:", shift)
else:
    print("Unrecognized command:", formatted_command)
