a = int(input("First nmbr"))
b = int(input("Second nmbr"))
c = int(input("Third nmbr"))
d = []
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])
input()