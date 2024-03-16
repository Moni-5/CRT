# write a program in whhich you take an integer input from user if that integer is divisible by 3 and 6 print good number ,if the integer is divisble by 2 and 7 then print their average number
# if the integer is divisible by 4 or 9 then print awesome number else bad number
num=int(input("enter the number:"))
if num%3==0 and num%6==0:
    print("good number")
elif num%2==0 and num%7==0:
    avg=4.5
    print("avg"+avg)
elif num%4==0 or num%9==0:
    print("awesome number")
else:
    print("bad number")
