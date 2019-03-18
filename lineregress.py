"""
X  Y  X-MX   Y-MY  Sq(X-MX)  (X-MX)(Y-MY)
1  2   -2   -2
2  4   -1   0
3  5    0   1
4  4    1   0
5  5    2   1
MX=3
MY=4
Step 2:
 find b1:
Step 3:
 find bo
Step 4:
 find error
"""
X = [1,2,3,4,5]
Y = [2,4,5,4,5]
Q = []
P = []
W = []
R = []
MX = sum(X)//5
MY = sum(Y)//5

for i in range(0,5):
    q = X[i]-MX
    p = Y[i] - MY
    P.append(p)
    Q.append(q)
for i in range(0,5):
    e = Q[i]*Q[i]
    W.append(e)
for i in range(0,5):
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

def fun(x):
    y = 2.2 + x*(0.6)
    return y
T = []
for i in range(0,5):
    t = fun(X[i])
    T.append(t)
#print(T)
SqP = []
O = []
SqO = []
for i in range(0,5):
    p1 = P[i]*P[i]
    SqP.append(p1)
#print(SqP)
for i in range(0,5):
    t1 = T[i]-MY
    O.append(t1)
#print(O)
for i in range(0,5):
    f = O[i]*O[i]
    SqO.append(f)
#print(SqO)

m = sum(SqO)
s = sum(SqP)
mse = m/s
print(mse)
