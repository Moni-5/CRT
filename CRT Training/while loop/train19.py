n=12345
count=0
flag=0
while n!=0:
    count=n%10
    n=n//10
    if count==5 or count==4 or count==3 or count==2 or count==1:
        flag=flag+1
print(flag)
    
