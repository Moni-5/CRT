#create a class ticket which will be the abstarct class inside that create a fun() "bookticket"
#which will be te abstract method and has nothing in it.create a class makemytrip which will use the
#book ticket function from ticket class to take te details such as name,phno,email,journeydate
#and displays a msg "tq for booking from makemytrip.". Cretae class IRCTC which uses the bookticket
#of ticket class and takes same details as makemytrip buut in the end it will give an optoin to user
#the user to select wether it is oneway or round trip.If the user option is round trip it again ask the user
#to return date as well and ten prints a msg "tq for choosing IRCTC " else "tq for choosing IRCTC"
#create a class indigo which takes all details as IRCTC and just asks which mode of transport u
#want to go in Train,bus,flight and displays "tq for choosing Indigo"

from abc import ABC, abstractmethod
class ticket(ABC):
    @abstractmethod
    def bookticket(self):
        pass
class makemytrip(ticket):
    def bookticket(self):
        input("enter your name:")
        input("enter your phno:")
        input("enter your mail id:")
        input("enter your journey date")
        print("Thank you for choosing MakeMyTrip!!")
class irctc(ticket):
    def bookticket(self):
        input("enter your name:")
        input("enter your phno:")
        input("enter your mail id:")
        input("enter your journey date")
        self.x=input("is your journey oneway or roundtrip:")
        if self.x in ["roundtrip"]:
            input("Enter your return journey date:")
            print("Thank you for choosing IRCTC!!!")
        else:
            print("Thank you for choosing IRCTC!!!")
class indigo(ticket):
    def bookticket(self):
        
        input("enter your name:")
        input("enter your phno:")
        input("enter your mail id:")
        input("enter your journey date")
        self.y=input("is your journey oneway or roundtrip:")
        if self.y in["roundtrip"]:
            input("Enter your return journey date:")
        self.z=input("enter the mode of your journey bus or train or flight:")
        print("Thank you for choosing Indigo!!!")
obj=makemytrip()
obj.bookticket()

obj1=irctc()
obj1.bookticket()

obj2=indigo()
obj2.bookticket()
        







        
