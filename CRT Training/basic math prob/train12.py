#calculate the sum of digits of number which is taken input from the user
num=int(input("enter the number:"))
sum=0
while num!=0:
    sum=sum+(num%10)
    num=num//10
print(sum)    
    
    
    
