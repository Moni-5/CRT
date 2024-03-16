#Inheritence

class Faculty:
    def __init__(self,fname,department,clgid):
        self.fname=fname
        self.department=department
        self.clgid=clgid
    def print_info(self):
        print("Faculty Info is :",self.fname,self.department,self.clgid)
obj=Faculty("Ramesh","Information_Technology","102040")
obj.print_info()

class IT(Faculty):
    pass
obj=IT("Ramadevi","Information_Technology","103050")
obj.print_info()
