# take a num input from user check if the sum of factors of that number is greater than the original num or not

n=int(input("enter a number"))
sum=0
for i in range (1,n):
    if n%i==0:
        sum=sum+i
if sum>n:
    print("yes")
else:
    print("no")
        
        
    
    
    
    
