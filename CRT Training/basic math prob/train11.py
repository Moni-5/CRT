#implement program for prime
num=int(input("enter a num:"))
for i in range (2,num//2):
        if num%i==0:
            print("it is not prime")
            break
else:
    print("a prime")
        
        
