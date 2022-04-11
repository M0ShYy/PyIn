import random

# list of the characters available
numbers = "0123456789"
lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symboles = "!#$%&"
charlist = numbers + lettres + symboles


def Salt():
    global charlist
    longueur = random.randrange(10,15)
    password = ""

    for j in range(0, longueur):                                        # foreach characters
        charnb = (random.randrange(len(charlist)))                      # take a random character in the list
        password = password + charlist[charnb]                          # append the characters
    return password
