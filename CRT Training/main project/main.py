from login_reg import *
from products import *
from order import *

class Main:
    def mine(self):
        newobj=LandR()
        newobj.name()
        newobj.register()
        newobj.login()
    
last=Main()
last.mine()
