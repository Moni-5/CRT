r=int(input())
for i in range (1,r+1):
    for j in range (1,i+1):
        print(i)
        if i==5:
            i=i-1
            print(j,end="")
    print()