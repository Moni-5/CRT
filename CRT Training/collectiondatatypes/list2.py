list=[12,42,23,96,7,18,10,133]
#addition of min and max value
max=list[0]
min=list[0]
for i in list:
    if i>max:
        max=i
        
    if i<min:
        min=i
        
add=max+min
sub=max-min
print(add)
print(sub)
list[max]=add
list[min]=sub
print(list)

    
