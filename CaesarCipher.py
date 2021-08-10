def shiftLetter(ch, baseChar, shiftValue):
    """ Translate a range of characters starting at baseChar down to 0 range,
    add the shiftValue modularly, and then translate back to original range. """
    shiftDownAndRotate = ((ord(ch) - ord(baseChar)) + shiftValue) % 26
    shiftUp = chr(shiftDownAndRotate + ord(baseChar))
    return shiftUp


def shiftUpperLetter(ch, shiftValue):
    """ Apply shifting to uppercase letters. """
    return shiftLetter(ch, 'A', shiftValue)


def shiftLowerLetter(ch, shiftValue):
    """ Apply shifting to lowercase letters. """
    return shiftLetter(ch, 'a', shiftValue)


def caesarCipherText(text, shiftValue):
    """ This applies the Caesar Cipher algorithm to text with the
        given shift value.  Notice that this is the same algorithm
        for encrypt and decrypt, only with different shift values.  """
    newtext = ""
    for ch in text:
        # Character is lower case letter:
        if ('a' <= ch <= 'z'):
            newtext += shiftLowerLetter(ch, shiftValue)
            # Character is upper case letter:
        elif ('A' <= ch <= 'Z'):
            newtext += shiftUpperLetter(ch, shiftValue)
            # Character is non-letter:
        else:
            newtext += ch
    return newtext



