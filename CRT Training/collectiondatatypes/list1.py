list=["a","b","c",10,20,30]
print(list)
print(list[2],list[4])
print(list[-1:])
print(list[::.-1])
print(list[1:6])
print(list[:4:2])
print(list[2:])
for i in list:
    print(i)
list.append(10)
print(list)
list.insert(4,"abc")
print(list)
multilist=[[1,2,3,4],["a","b","c","d"]]
print(multilist)
print(multilist[1][3])
multilist.insert(20,12)
print(multilist)

