r=int(input())
for i in range (1,r+1):
    for s in range (1,(r-i)+1):
        print(" ", end="")
    for j in range (1,2*i):
        print("*", end="")
    print()
