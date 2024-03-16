#create a class of name placements which has fun() "info" which displays the no of placements this
#year. create another class name department wit fun() "display" which will display the names of departments
#present in the college. create a class pragati with a fun() "welcome" which displays te message
# welcome to prag college we are glad ave you on board . pragati class should also display the
# details avout deparments and placements...

class placements:
    def info(self):
        print("The number of placements this year are 750 and still counting!!!!")
class department:
    def display(self):
        print("The departmenst present in our college are:")
        print("1.CSE 2.IT 3.AIML 4.CIVIL 5.MECH 6.ECE 7.EEE")
class Pragati(placements,department):
    def welcome(self):
        print("Welcome to Pragati Engineering College.We are glad to have you on board")
        obj.display()
        obj.info()
obj=Pragati()
obj.welcome()

