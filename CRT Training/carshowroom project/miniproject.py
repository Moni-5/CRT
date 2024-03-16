# when car compamy and car model is selected the details of on road price and
#its mileage should be displayed to the user
#toyota ,mahindra,mercedes(car companies)
#take the input from user for the car company name and in the input message give the
#option of three companies this user input companu name goes as the
#input/argument to model name function , which welcomes te user accordingly to
#the company name, ask the user to enter the specific model name for that company.
#the second function variant(). according to the car company name and car model the usr should
#be ask to enter the variant he would likes to choose from petrol,diseal
#the last function display() according to the car company ,car model name and car variant
#first its ex showroom price should be displayed and then its on road price should be displayed
#which is calculated as ex showroom price +cgst+sgst+insurance. The sgst ,cgst and the insurance
#all the three have a common value throughout the car showroom

class Myshowroom:
    def __init__ (self):
        print("Hello Customer, Welcome to Car showroom!!")
        print('We have wide range of company select any 1.Mahindra,2.Toyota,3.Mercedes')
    def showroom(self):
        
        com=(input("Enter the car company from the above mentioned list:"))
        
        if com in ["Mahindra", "1"]:
            self.com=com
        elif com in["Toyota" ,"2"]:
            self.com=com
        elif com in ["Mercedes" , "3"]:
            self.com=com
        else:
            print("Please enter a valid company car")
            cust.showroom()
           
    def companyname(self):
    
        if self.com in ["Mahindra", "1"]:
            model=input(("Enter the modelof 1.Thar or 2.XUV300 or 3.KUV100:"))
            if model in["Thar", "1"]:
                self.model=model
            elif model in ["XUV300" , "2"]:
                self.model=model
            elif model in ["KUV100","3"]:
                self.model=model
            else:
                print("Please enter a valid model")
                cust.companyname()
                
        elif self.com in ["Toyota", "2" ]:
            model=input(("Enter the model 1.Glanza or 2.Urban Cruiser or 3.Inova Crysta:"))
            if model in["Glanza" ,"1"]: 
                self.model=model
            elif model in["Urban Cruiser","2"]:
                self.model=model
            elif model in["Inova Crysta","3"]:
                self.model=model
            else:
                print("Please enter valid model")
                cust.companyname()
        elif self.com in["Mercedes" ,"3"]:
            model=input(("Enter the model 1.GLE LWB or 2.E-Class or 3.G Wagon:"))
            if model in["GLE LWB" , "1"]: 
                self.model=model
            elif model in["E-Class" , "2"]:
                self.model=model
            elif model in["G Wagon","3"]:
                self.model=model
            else:
                print("Please enter a valid model")
                cust.companyname()
        else:
            print("Please enter a valid input")
    def variant(self):
        var=input(("Enter the specific of 1.petrol or 2.diesel "))
        if var in ["petrol" , "1"]: 
            self.var=var
        elif var in["diesel" , "2"]:
            self.var=var
        else:
            print("Please enter a valid varient")
            cust.variant()
    def display(self):
        if self.com in["Mahindra" , "1"] and self.model in["Thar" , "1"]:
            
            if self.var in["petrol" , "1" ]:
                exshowprice=600000
                tax=exshowprice*(20/100)
            elif self.var in["diesel" "2"]:
                exshowprice=650000
                tax=exshowprice*(20/100)
            
        elif self.com in["Mahindra" , "1"]  and self.model in["XUV300", "2"]  :
            if self.var in["petrol" , "1" ]:
                exshowprice=630000
                tax=exshowprice*(20/100)
            elif self.var in["diesel" "2"]: 
                exshowprice=700000
                tax=exshowprice*(20/100)
        elif self.com in["Mahindra" , "1"] and self.model in["KUV100" , "3"]:
            
            if self.var in["petrol" , "1" ]:
                exshowprice=540000
                tax=exshowprice*(20/100)
            elif self.var in["diesel" "2"]:
                exshowprice=590000
                tax=exshowprice*(20/100)
        elif self.com in ["Toyota", "2" ] and self.model in ["Glanza" , "1"] :
            if self.var in["petrol" , "1" ]:
                exshowprice=750000
                tax=exshowprice*(20/100)
            elif self.var in["diesel", "2"]: 
                exshowprice=800000
                tax=exshowprice*(20/100)
        elif self.com in ["Toyota", "2" ]  and self.model in["Urban Cruiser" , "2"] :
            if self.var in["petrol" , "1" ]:
                
                exshowprice=853000
                tax=exshowprice*(20/100)
            elif self.var in["diesel", "2"]:
                exshowprice=754000
                tax=exshowprice*(20/100)
        elif self.com in ["Toyota", "2" ] and self.model in ["Inova Crysta" , "3"] :
            if self.var in["petrol" , "1" ]:
                exshowprice=780000
                tax=exshowprice*(20/100)
            elif self.var in["diesel", "2"]:
                exshowprice=7650000
                tax=exshowprice*(20/100)
        elif self.com in ["Mercedes","3"]  and self.model in["GLE LWB" , "1"]:
            if self.var in["petrol" , "1" ]:
                exshowprice=9500300
                tax=exshowprice*(25/100)
            elif self.var in["diesel", "2"]:
                exshowprice=9600452
                tax=exshowprice*(20/100)   
        elif self.com in ["Mercedes","3"]  and self.model in ["E-Class" , "2"]:
            if (self.var=="petrol"):
                exshowprice=1050000
                tax=exshowprice*(20/100)
            elif(self.var=="diesel"):
                exshowprice=1043000
                tax=exshowprice*(20/100)
        elif self.com in ["Mercedes","3"]  and self.model in["G Wagon" , "3"]:
            if self.var in["petrol" , "1" ]:
                exshowprice=9700300
                tax=exshowprice*(20/100)
            elif self.var in["diesel", "2"]:
                exshowprice=10000452
                tax=exshowprice*(20/100)   
        
        on_roadprice=exshowprice+(3*tax)
        print("The exshowroom price of car company",self.com,"of the model",self.model,"in",self.var,"variant is",exshowprice)
        print("The onroadprice of car company",self.com,"of the model",self.model,"in",self.var,"varient is",on_roadprice)
cust=Myshowroom()
cust.showroom()
cust.companyname()
cust.variant()
cust.display()
