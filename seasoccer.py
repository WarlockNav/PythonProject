import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("FullData.csv")
#print(df)
"""
plt.figure(figsize=(30,20))
sns.countplot(y = df.Nationality, palette = "Set2")
plt.show()
"""
"""
plt.figure(figsize=(15,10))
sns.countplot(x = "Club_Position",data=df)
plt.show()
"""
#Case Study
#print(df["GK_Handling"])
w1 = 2
w2 = 2
w3 = 1
w4 = 3
w5 = 2
df["GK_Shot_Stopper"] = (w1*df.GK_Positioning + w2*df.GK_Diving + w3*df.GK_Kicking + w4*df.GK_Handling + w5*df.GK_Reflexes)
sortedDf = df.sort_values("GK_Shot_Stopper")
print(sortedDf.head(5))
print()
print(sortedDf.tail(5)) # Best 5 GoalKeepers
plt.figure(figsize=(30,20))
sns.countplot(x="Nationality",data =sortedDf)
plt.show()

