photo = [ [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]]
          ]
photo1 = [ [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]]
           ]
for i in range(0,len(photo)):
    for j in range(0,len(photo[i])):
        photo1[i][j] = photo[j][i]
print("Photo before rotation is :",photo)
print("Photo after rotation to the right at 90 degress is :",photo1)
