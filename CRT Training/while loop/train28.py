#1578 = 1^1+5^2+7^3+8^4
n=1578
n1=n
flag=0
rev=0
sod=0
while n!=0:
    x=n%10
    rev=rev*10+x
    n=n//10
while n1!=0:
    rev=n1%10
    flag=flag+1
    sod=sod+rev**flag
    n1=n1//10
print(sod)
