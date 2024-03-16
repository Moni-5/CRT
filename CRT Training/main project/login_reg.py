import csv
from products import *
from order import *
class LandR:
    def fname(self):
        self.x=self.name
        self.y=self.phno
        self.z=self.mail
        self.q=self.addres
    def name(self):
        self.name=input("Enter your name:")
        self.phno=input("Enter your PHno:")
        self.mail=input("Enter your mail:")
        self.addres=input("Enter your address:")
        print("Set a Username and Password for your account")
    def register(self):
        f=open('Login.csv','a',newline='')
        a=csv.writer(f)
        a.writerow(['self.user','self.password'])
        self.user=input("Enter the user name:")
        self.password=input("Enter the password:")
        self.confirm=input("Renter your password:")
        print("Password conformation")
        
        if self.password == self.confirm:
            print("User succesfully Registered")
            a.writerow([self.user,self.password])   
        else:
            print("Password Mismatched Enter same password twice")
            o1.register()
            
    def login(self):
        print("Login Page")
        self.x=input("Enter User name:")
        self.y=input("Enter Password:")
        with open('Login.csv','r',newline='') as file:
            read=csv.DictReader(file)
            for row in read:
                if self.user==self.x and self.password==self.y:
                    print("Login Succesful, Happy Shopping")
                    o2=Product()
                    o2.pro()
                else:
                    print("Invalid credentials, Try Again!!")   
o1=LandR()


                