photo = [ [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]]
          ]
print(len(photo))
photo1 = [ [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]]
           ]

"""
for i in range(0,len(photo)):
    print(i)
    
    for j in range(0,len(photo[i])):
        print(j)
        photo[i][j] = photo[j][i]
        print(photo)
"""
photo[0][1] = photo1[1][0]
photo[0][2] = photo1[2][0]
photo[1][0] = photo1[0][1]
photo[1][2] = photo1[2][1]
photo[2][0] = photo1[0][2]
photo[2][1] = photo1[1][2]
print("Before rotation the photo is : ",photo1)
print("After rotation to the 90 degrees right the photo is : ",photo)

