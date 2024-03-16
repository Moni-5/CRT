#armstrong number
num=int(input("enter a number:"))
sum=0
temp=num
digits=0
while num!=0:
    x=num%10
    digits=3
    sum=sum+x**digits
    num=num//10
if sum==temp:
    print("armstrong")
else:
    print("not a armstrong")
    
    
