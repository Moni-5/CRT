#rwite a fun() to calciulate sum of first and last digit of a num
def fun5(num):
    x=num%10
    y=num//10
    while y>=10:
        z=y//10
        sum=x+z
        print(sum)
fun5(152)
