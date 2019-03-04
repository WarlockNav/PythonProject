
a = [5000,2500,1600,300,2000,100]
b = [40,20,6,4,3,2]
cost = 0
c = []
d = []
for i in range(0,6):
    cost = a[i]//b[i]
    c.append(cost)
    cost = 0
#print(c)
#for j in range(0,6):
d.append(max(c))
for j in range(0,6):
    if d[0] == c[j]:
        e = b[j]
f=e

for e in range(0,41):
    if e < 40:

        e = e + e
        cost = cost + d[0]

#print(e)
#print(d)
#print(e)
#print(cost)
print("Maximum profit is :",cost,"for value",f)
