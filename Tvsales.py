import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("advert.csv")
X = data["TV"].values
Y = data["Sales"].values
Q = []
P = []
W = []
R = []
MX = sum(X)//len(X)
MY = sum(Y)//len(Y)

for i in range(0,len(X)):
    q = X[i]-MX
    p = Y[i] - MY
    P.append(p)
    Q.append(q)
for i in range(0,len(X)):
    e = Q[i]*Q[i]
    W.append(e)
for i in range(0,len(X)):
    a = Q[i]*P[i]
    R.append(a)

#print(Q)
#print(P)
#print(W)
#print(R)
SumSq = sum(W)
SumProduct = sum(R)
#print(SumSq)
#print(SumProduct)

b1 = SumProduct/SumSq
#print(b1)
b0 = MY-b1*MX
def fun(x):
    global b0
    global b1
    y = b0 + x*(b1)
    return y
T = []
for i in range(0,len(X)):
    t = fun(X[i])
    T.append(t)
#print(T)
SqP = []
O = []
SqO = []
for i in range(0,len(X)):
    p1 = P[i]*P[i]
    SqP.append(p1)
#print(SqP)
for i in range(0,len(X)):
    t1 = T[i]-MY
    O.append(t1)
#print(O)
for i in range(0,len(X)):
    f = O[i]*O[i]
    SqO.append(f)
#print(SqO)

m = sum(SqO)
s = sum(SqP)
mse = m/s
print(mse)
