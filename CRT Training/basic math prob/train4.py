# write a program to accept one single sub marks from the user then check if te marks are >35 print cheated if =35 print pass if <35 print fail
marks=int(input("enter the marks of the subject:"))
if marks>35:
       print("cheated")
elif marks==35:
    print("pass")
else:
    print("fail")
