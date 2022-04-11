from getpass import getpass
import Fonctions

DB = 'DB.csv'


action = input('1 = Sign Up \n2 = Sign In : ')

if action == "1":
    username = input("Username : ")
    if Fonctions.testuser(DB, username):
        print("The password have to contain Min ten Chars, One Upper, One Lower, One symbole and One Number")
        passwd = getpass()
        confpasswd = getpass("confirm Password: ")
        if Fonctions.testPass(passwd, confpasswd):
            if Fonctions.testPassStrength(passwd):
                Fonctions.signup(DB, username, passwd)
        else:
            print("the passwords are not identical")
        print("finish")
    else:
        print('the username already exist')
elif action == "2":
    username = input("Username : ")
    passwd = getpass()
    Fonctions.signin(DB, username, passwd)
else:
    print("please enter 1 OR 2")
