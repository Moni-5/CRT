#write rec fun to calculate te sum of digits of num
def sum(n1):
    if n1==0:
        return 0
    else:
        s=n1%10
        return s+sum(n1//10)
        
print(sum(123))

