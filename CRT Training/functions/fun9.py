# wirte the recursive prog to print the digits in reverse order
def rev(n1):
    n=n1
    if n1==0:
        return 0
    else:
        n1=n1%10
        print(n1)
        while n!=0:
            rev(n//10)
rev(123)
    

    
