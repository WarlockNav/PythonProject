photo = [ [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]]
          ]
photo1 = []
for i in range(0,len(photo)):
    total = 0
    for j in range(0,len(photo[i])):
        for k in range(0,len(photo[j])):
            total = total + photo[i][j][k]
        #print(total//3)
        photo1.append(total//3)
        total = 0
print("Before Gray Scaling the photo is:")
print(photo)
def grayscale():
    photo[0][0][0] = photo1[0]
    photo[0][0][1] = photo1[0]
    photo[0][0][2] = photo1[0]
    photo[0][1][0] = photo1[1]
    photo[0][1][1] = photo1[1]
    photo[0][1][2] = photo1[1]
    photo[0][2][0] = photo1[2]
    photo[0][2][1] = photo1[2]
    photo[0][2][2] = photo1[2]
    photo[1][0][0] = photo1[3]
    photo[1][0][1] = photo1[3]
    photo[1][0][2] = photo1[3]
    photo[1][1][0] = photo1[4]
    photo[1][1][1] = photo1[4]
    photo[1][1][2] = photo1[4]
    photo[1][2][0] = photo1[5]
    photo[1][2][1] = photo1[5]
    photo[1][2][2] = photo1[5]
    photo[2][0][0] = photo1[6]
    photo[2][0][1] = photo1[6]
    photo[2][0][2] = photo1[6]
    photo[2][1][0] = photo1[7]
    photo[2][1][1] = photo1[7]
    photo[2][1][2] = photo1[7]
    photo[2][2][0] = photo1[8]
    photo[2][2][1] = photo1[8]
    photo[2][2][2] = photo1[8]
    print("After Gray scaling the photo is:")
    print(photo)
grayscale()
