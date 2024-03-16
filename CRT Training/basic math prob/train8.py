#write a prog to ceck the type of triangle where you take input from user for three sides and classify it accordingly intlo equilateral,scalene,isosceles
s1=int(input("enter side 1:"))
s2=int(input("enter side 2:"))
s3=int(input("enter side 3:"))
if s1==s2 and s2==s3:
    print("it is eqilateral trinagle")
elif s1==s2 and s2!=s3:
    print("it is isoceles triangle")
else:
    print("it is scalene triangle")
