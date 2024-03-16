class Authenticate:
    def user(self):
        self.x=input("Enter the username:")
        self.y=input("Enter the password:")
        if self.x==self.y:
            print("Successful Login")
            print("Select any one Following option")
            print("1.CheckBalance")
            print("2.Cashwithdrawl")
            print("3.Cashdeposit")
            print("4.Ministatement")
        else:
            print("Enter the valid options")

        
        
            
