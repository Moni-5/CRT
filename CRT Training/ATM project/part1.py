from part2 import Authenticate
class Atm:
    def __init__(self,atmbalance):
        self.atmbalance=atmbalance
        print("Welcome to the ATM")
        print("The amount present in the ATM currently is :",self.atmbalance)
        print("Select the account you want to withdraw from")
        print("1.Rupay")
        print("2.Visa")
        print("3.Mastercard")
    def account(self):
        self.x=input("Enter any one account:")
        if self.x in ["1","2","3","Rupay","Visa","Mastercard"]:
            authobj=Authenticate()
            authobj.user()
            
        else:
            print("Enter Valid Acoount")
            o1.account()
o1=Atm(1000000)
o1.account()
