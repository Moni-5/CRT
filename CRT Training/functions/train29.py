#write a fun() which takes two parameters  a and b typecast the value of 2nd argument into
#integer then multiply both the arguments and print the last digit of the result
def typecast(a,b):
    c=int(b)
    d=a*c
    e=d%10
    print(e)
typecast(10,"5")
    
