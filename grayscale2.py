photo = [ [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]]
          ]
photo1 = []
photo2 = [ [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]]
          ]
for i in range(0,len(photo)):
    total = 0
    for j in range(0,len(photo[i])):
        for k in range(0,len(photo[j])):

            total = total + photo[i][j][k]
        #print(total//3)
        photo1.append(total//3)
        total = 0
for l in range(0,len(photo)):
    for m in range(0,len(photo[l])):
        for n in range(0,len(photo[m])):
            photo[l][m][n] = photo1[m]
#print(photo1)
print("Photo Before Gray Scaling is: ")
print(photo2)
print("Photo after Gray Scaling is : ")
print(photo)
