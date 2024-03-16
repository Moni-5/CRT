def con(n):
    if n==0:
        return 0
    return 1+con(n//10)
def pow(n,count):
    if n==0:
        return 0
    return (n%10)**count+pow(n//10,count)
n=int(input())
count=con(n)
res=pow(n,count)
if (res==n):
    print("yes")
else:
    print("no")
        
        
