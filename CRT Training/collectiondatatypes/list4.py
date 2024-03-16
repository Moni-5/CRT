list=[2,0,1024,0,40,230,0]
#while maintaing the order shift the zeros to right side


a=0
for i in list:
    if i==a:
        list.remove(i)
        list.append(0)    
print(list)

......................................
res=[]
count=0
for i in list:
    if i==0:
        count=count+1
    else:
        res.append(i)
res=res+[0]*count
print(res)
