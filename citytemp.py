import pandas as pd
df1 = pd.read_csv('temp.txt')
print(df1)
df = pd.read_csv('temp.txt', delim_whitespace=True, usecols=range(2,5))
b = df.mean()
print(b)
mn = []
mn.append(b[0])
mn.append(b[1])
mn.append(b[2])
print(mn)
print(type(mn))
if mn[0]<mn[1]:
    if mn[0]<mn[2]:
        print("ludhiana is coolest")
elif mn[1]<mn[2]:
    print("Amritsar is coolest")
if mn[2]>mn[1]:
    print("Chandigarh is hottest")
