data="aaa^111\nbbb^222\nccc^333"
fm=data.split("\n")
print(fm)
a=[]
b=[]
for i in fm:
    #print(i)
    k=i.split("^")
    a.append(k[0])
    b.append(k[1])

print(a)
print(b)

