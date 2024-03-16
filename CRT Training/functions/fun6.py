#wriet a login fun which accpets the user onlly when the username and password are
#same and displays a msg login successful other wise it keeps asking te user to enter the credentials
#until they are correct
def login():
    username=input("enter the username:")
    password=input("enter the password:")
    if username==password:
        print("succesful login")
    else:
        print("login unsuccessful")
        print("enter the credentials again")
        while username!=password:
            login()
            break
login()
            
def login():
    while True:
        username=input("enter the username:")
        password=input("enter the password:")
        if username==password:
             print("succesful login")
             break
        else:
             print("login unsuccessful")
             print("enter the credentials again")
login()
         
