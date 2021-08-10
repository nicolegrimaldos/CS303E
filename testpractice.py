def essayCharacterCount(sent, dontCount):
    # Write your code here
    sent= sent.lower()
    sent = sent.split(" ")
    sub = 0
    max = 0
    for x in sent:
        max += len(x)
        for n in dontCount:
            if n == x:
                sub += len(n)
    characterCount = max - sub
    return characterCount


def comparingPopulations(populations):
    # Write your code here
    first = 0
    second = 0
    third = 0
    for x in populations:
        if populations[x] > first:
            first = populations[x]
            firstName = ( str(x) + " - " + str(populations[x]))
    for x in populations:
        if populations[x] < first and populations[x] > second :
            secondName = ( str(x) + " - " + str(populations[x]) )
            second = populations[x]
    for x in populations:
        if populations[x] < second and populations[x] > third:
            third = populations[x]
            thirdName = ( str(x) + " - " + str(populations[x]))
    print("1.",firstName)
    print("2.",secondName)
    print("3.",thirdName)


def removeLonelyNumbers(lst):
    # Write your code here
    x = 1
    newList = lst
    if len(lst)<= 1:
        return newList
    while x != len(lst)-1:
        if lst[x] != lst[x-1] and lst[x] != lst[x+1] :
            if lst[x-1] > lst[x+1] :
                newList[x] = lst[x-1]
            else:
                newList[x] = lst[x+1]
        x += 1
    return newList


def substringCount(str, substring):
    # Write your code here
    count = 0
    str = str.split(substring)
    for x in str:
        if x == "":
            count += 1
    return count



def stringWithStars(str):
    # Write your code here
    n = 0
    if len(str) <= 1:
        return str
    else:
        return str[0] + "*" + stringWithStars(str[1:])

    def cleanString(str):
        # Write your code here
        # Write your code here
        x = 1
        newString = str[0]
        if len(str) < 2:
            return newString
        else:
            # yyzzza
            if str[0] == str[1]:
                return cleanString(str[1:])
            else:
                return str[0] + cleanString(str[1:])


def reverseLookUp(dict, value):
    # Write your code here
    new = []
    for x in dict:
        if dict[x] == value:
            new.append(x)
    return new



