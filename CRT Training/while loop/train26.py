#palindrome number
num=int(input("enter a num:"))
tem=num
rev=0
while num!=0:
    x=num%10
    rev=rev*10+x
    num=num//10
if (tem==rev):
    print("palindrome")
else:
    print("not palindrome")
