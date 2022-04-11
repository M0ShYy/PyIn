from getpass import getpass
import csv
import Salt_Generator
import hashlib
DB = 'DB.csv'


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
                print('user trouvé: ')
                password = password + lines["Salt"]
                password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if password == lines["Password"]:
                    print("Bon MDP")
                    print(f"bienvenue {user}")
                else:
                    print("Mauvais MDP")
                break
        file.close()


def signup(file, user, password):
    Salt = Salt_Generator.Salt()
    password = password + Salt
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    data = [user, password, Salt]
    WriteCSV(file, data)


action = input('1 = Sign Up \n2 = Sign In : ')

if action == "2":
    username = input("Username : ")
    passwd = getpass()
    signin(DB, username, passwd)
elif action == "1":
    username = input("Username : ")
    if testuser(DB, username):
        passwd = getpass()
        confpasswd = getpass("confirm Password: ")
        if testPass(passwd, confpasswd):
            signup(DB, username, passwd)
        else:
            print("the passwords are not identical")
        print("finish")
    else:
        print('the username already exist')
else:
    print("please enter 1 OR 2")
