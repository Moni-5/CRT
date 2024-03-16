dict={"a":11,"b":12,"c":13,"d":13}
print(dict)
print(dict["a"],dict["b"])
dict["a"]=20
print(dict)
for i in dict:
    print(dict[i])
del dict["a"]
print(dict)
