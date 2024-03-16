import csv
from order import Order
class Product:
    def clothing(self):
        print("1.Jeans")
        print("2.Shirts")
        print("3.KurtaSet")
        self.b=input("Enter the product you want:")
        while True:
            if self.b in ["1","Jeans"]:
                self.c=10
                self.price=800
                print("Price of Jeans:800/-")
                print("Quantity present:10")
                self.d=int(input("Enter the Quantity:"))
                if self.d<=self.c:
                    self.cost=self.price*self.d
                    print("The total cost of product is:",self.cost)
                else:
                    print("Enter Valid quantity")
            elif self.b in ["2","Shirts"]:
                self.c=10
                self.price=1200
                print("Price of Shirt:1200/-")
                print("Quantity present:10")
                self.d=int(input("Enter the Quantity:"))
                if self.d<=self.c:
                    self.cost=self.price*self.d
                    print("The total cost of product is:",self.cost)
                    newobj2=Order()
                    newobj2.place()
                else:
                    print("Enter Valid quantity")
            elif self.b in ["3","Kurtaset"]:
                self.c=10
                self.price=2500
                print("Price of Kurtaset:2500/-")
                print("Quantity present:10")
                self.d=int(input("Enter the Quantity:"))
                if self.d<=self.c:
                    self.cost=self.price*self.d
                    print("The total cost of product is:",self.cost)
                    newobj2=Order()
                    newobj2.place()
                else:
                    print("Enter Valid quantity")
    def mobile(self):
        print("1.OnePlus12R")
        print("2.Pixel")
        print("3.Iphone")
        self.b=input("Enter the product you want:")
        while True:
            if self.b in ["1","Oneplus12R"]:
                self.c=10
                self.price=59999
                print("Price of Oneplus12R:59999/-")
                print("Quantity present:10")
                self.d=int(input("Enter the Quantity:"))          
                if self.d<=self.c:
                    self.cost=self.price*self.d
                    print("The total cost of product is:",self.cost)
                    newobj2=Order()
                    newobj2.place()
                else:
                    print("Enter Valid quantity")
            elif self.b in ["2","Pixel"]:
                self.c=10
                self.price=76999
                print("Price of Pixel:76999/-")
                print("Quantity present:10")
                self.d=int(input("Enter the Quantity:"))
                if self.d<=self.c:
                    self.cost=self.price*self.d
                    print("The total cost of product is:",self.cost)
                    newobj2=Order()
                    newobj2.place()
                else:
                    print("Enter Valid quantity")
            elif self.b in ["3","Iphone"]:
                self.c=10
                self.price=89499
                print("Price of Iphone:89499/-")
                print("Quantity present:10")
                self.d=int(input("Enter the Quantity:"))
                if self.d<=self.c:
                    self.cost=self.price*self.d
                    print("The total cost of product is:",self.cost)
                    newobj2=Order()
                    newobj2.place()
                else:
                    print("Enter Valid quantity")
    def electronic(self):
        print("1.Computer")  
        print("2.Earpods") 
        print("3.TV")
        self.b=input("Enter the product you want:")
        if self.b in ["1","Computer"]:
            self.c=10
            self.price=15499
            print("Price of Computer:15499/-")
            print("Quantity present:10")
            self.d=int(input("Enter the Quantity:"))
            if self.d<=self.c:
                self.cost=self.price*self.d
                print("The total cost of product is:",self.cost)
                newobj2=Order()
                newobj2.place()
                newobj2.new()
            else:
                print("Enter Valid quantity")
        elif self.b in ["2","Earpods"]:
            self.c=10
            self.price=1299
            print("Price of Earpods:1299/-")
            print("Quantity present:10")
            self.d=int(input("Enter the Quantity:"))
            if self.d<=self.c:
                self.cost=self.price*self.d
                print("The total cost of product is:",self.cost)
                newobj2=Order()
                newobj2.place()
            else:
                print("Enter Valid quantity")
        elif self.b in ["3","TV"]:
            self.c=10
            self.price=45000
            print("Price of TV:45000/-")
            print("Quantity present:10")
            self.d=int(input("Enter the Quantity:"))
            if self.d<=self.c:
                self.cost=self.price*self.d
                print("The total cost of product is:",self.cost)
                newobj2=Order()
                newobj2.place()
            else:
                print("Enter Valid quantity")
    def pro(self):
        print("Products Page")
        print("Categories: 1.Clothing  2.Mobiles 3.Electronics")
        self.a=input("Enter the Category:")
        if self.a in ["Clothing","1"]:
            o2.clothing()
        elif self.a in ["Mobiles","2"]:
            o2.mobile()
        elif self.a in ["Electronics","3"]:
            o2.electronic()
o2=Product()