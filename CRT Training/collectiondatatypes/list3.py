list=[22,42,65,1,-4,6,-1]
#write a prog to find the second smallest -ve num from list witout using sort & max ,min

m=list[0]
sm=0
for i in list:
    if i<=m:
        m,sm=i,m
    elif sm>i and m>sm:
        sm=i
    else:
        i=sm
print(sm)
        
    
