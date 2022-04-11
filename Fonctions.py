import random
import csv
import hashlib

# list of the characters available
numbers = "0123456789"
Llettres = "abcdefghijklmnopqrstuvwxyz"
Uletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symboles = "!#$%&_-.:"
charlist = numbers + Llettres + Uletters + symboles


def Salt():
    longueur = random.randrange(10, 15)
    password = ""

    for j in range(0, longueur):                                        # foreach characters
        charnb = (random.randrange(len(charlist)))                      # take a random character in the list
        password = password + charlist[charnb]                          # append the characters
    return password


def testuser(file, user):
    test = True
    with open(file, mode='r') as Ufile:
        # reading the CSV file
        csvFile = csv.DictReader(Ufile)

        # displaying the contents of the CSV file
        for lines in csvFile:
            if user in lines["Username"]:
                test = False
                break
    return test


def testPass(passwd, confpasswd):
    test = True
    if passwd != confpasswd:
        test = False
    return test


def testPassStrength(password):
    Upper = False
    Lower = False
    Number = False
    symbols = False
    if len(password) <= 10:
            print("Your password is to short (Min 10 chars)")
    else:
        for i in password:
            if i in Uletters:
                Upper = True
            elif i in Llettres:
                Lower = True
            elif i in numbers:
                Number = True
            elif i in symboles:
                symbols = True
        if not Upper:
            print("You have to have min ONE Uppercase lettre")
            return False
        elif not Lower:
            print("You have to have min ONE Lowercase lettre")
            return False
        elif not Number:
            print("You have to have min ONE Number")
            return False
        elif not symbols:
            print("You have to have min ONE symbole (!#$%&_-.:)")
        else:
            print("Valid Password")
            return True




def WriteCSV(file, data):
    with open(file, 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = csv.writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data)

        # Close the file object
        f_object.close()


def signin(file, user, password):
    with open(file, mode='r') as file:
        # reading the CSV file
        csvFile = csv.DictReader(file)

        # displaying the contents of the CSV file
        for lines in csvFile:
            if user in lines["Username"]:
                print('user find: ')
                password = password + lines["Salt"]                                 # appending the salt to the password
                password = hashlib.sha256(password.encode('utf-8')).hexdigest()     # hashing the password+ salt
                if password == lines["Password"]:
                    print("Good Password")
                    print(f"Welcome {user}")
                else:
                    print("wrong Password")
                break
        file.close()


def signup(file, user, password):
    salt = Salt()                                                                   # create a Salt
    password = password + salt                                                      # appending the salt to the password
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()                 # hashing the password+ salt
    data = [user, password, salt]
    WriteCSV(file, data)    # write the data il the csv file
