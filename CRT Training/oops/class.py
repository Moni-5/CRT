#create a class f15 with fun()lights("the color of light which is taken as paraeter to the fun"),
#fans("it displays the speed of regulator,which is taken as paramter of fun()") and
#AC ("displays room temp and the outside temp,which are taken as parameters")
#write a 4th fun display("displays diff in outside temp and room temp of AC and also displays fan speed")

class f15:
    def lights(moni,color):
        moni.color=color
        print("the color of light is:",color)
    def fans(moni,speed):
        moni.speed=speed
        print("the speed of regulator is :",speed)
    def ac(moni,roomtemp,outtemp):
        moni.roomtemp=roomtemp
        moni.outtemp=outtemp
        print("the room temp is:",roomtemp)
        print("the out temp is:",outtemp)
    def display(moni):
        diff=moni.outtemp-moni.roomtemp
        print("the diff in temp is:",diff)
        print("the speed of reguator is:",moni.speed)
stud=f15()
stud.lights("white")
stud.fans(150)
stud.ac(25,35)
stud.display()


        
