import numpy as np

choice = int(input("Enter your choice -> 4 by 4 Chess or 8 by 8 Chess,Press 4 or 8!!"))
if choice ==4:
    arr = np.zeros((4, 4))
    arr1 = np.asarray(arr)
    print("Your Chess ->", arr1)
    print("+++++++++++++++++")
    print("Queen should be placed like this->>")
    np.asarray(arr1)[0][1] = 1
    np.asarray(arr1)[1][3] = 1
    np.asarray(arr1)[2][0] = 1
    np.asarray(arr1)[3][2] = 1
    print(arr1)
elif choice == 8:
    arr = np.zeros((8, 8))
    arr1 = np.asarray(arr)
    print("Your Chess ->", arr1)
    print("+++++++++++++++++")
    print("Queen should be placed like this->>")
    np.asarray(arr1)[0][2] = 1
    np.asarray(arr1)[1][4] = 1
    np.asarray(arr1)[2][1] = 1
    np.asarray(arr1)[3][7] = 1
    np.asarray(arr1)[4][0] = 1
    np.asarray(arr1)[5][6] = 1
    np.asarray(arr1)[6][3] = 1
    np.asarray(arr1)[7][5] = 1
    print(arr1)
    print(arr1)


