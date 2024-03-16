class f15:
    def __init__(moni,stime,etime):
        moni.stime=stime
        moni.etime=etime
        print("I am the one who first noticed her")
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
        print("the start time is:",moni.stime)
        print("the end time is:",moni.etime)
stud=f15(9.0,16.0)
stud.lights("white")
stud.fans(150)
stud.ac(25,35)
stud.display()
