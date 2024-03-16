# take an integer as an input from the user and check whether if the number is
# divisible by its sum of digits or not

num=int(input("enter a num:"))
n=num
sum=0
while num!=0:
    sum=sum+ (num%10)
    num=num//10
if n%sum==0:
    print("divisible")
else:
    print("not divisible")
