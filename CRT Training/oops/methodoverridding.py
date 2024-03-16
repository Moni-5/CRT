#method overridding
class father:
    def bike(self):
        print("harley Davidson")
    def lappy(self):
        print("lappy wot basic configuration")
class son(father):
    def lappy(self):
        print("lappy with high configuration")
obj= son()
obj.bike()
obj.lappy()
