import pandas as pd
import matplotlib.pyplot as plt
import math
data = pd.read_csv("entropy.csv")
val = data["play"].values
#print(val)
#print(type(val))
#print(len(val))
a = 0
b = 0
for i in range(0,len(val)):
    #print(val[i])
    if val[i] == "yes":
        a = a+1
    elif val[i] == "no":
        b = b+1
#print(a)
#print(b)
e1 = a/len(val)
e2 = b/len(val)
#print(e1)
#print(e2)
e3 = math.log(e1,2)
e4 = math.log(e2,2)
#print(e3)
#print(e4)
E1 = -e1*e3
E2 = -e2*e4
#print(E1)
#print(E2)
E = E1 + E2
#print(E)
def GainOut():
    global val
    global E
    outlook1 = data["outlook"].values
    # print(outlook1)
    sunny = []
    rainy = []
    overcast = []
    for i in range(0, len(outlook1)):
        if outlook1[i] == "sunny":
            sunny.append(val[i])
        elif outlook1[i] == "rainy":
            rainy.append(val[i])
        elif outlook1[i] == "overcast":
            overcast.append(val[i])
    # print(sunny)
    # print(rainy)
    # print(overcast)
    c = 0
    d = 0
    for i in range(0, len(sunny)):
        if sunny[i] == "yes":
            c = c + 1
        elif sunny[i] == "no":
            d = d + 1
    # print(c)
    # print(d)
    y = c / len(sunny)
    y1 = math.log(y, 2)
    v = d / len(sunny)
    y2 = math.log(v, 2)
    S1 = -y * y1
    S2 = -v * y2
    S = S1 + S2
    # print(S)
    f = 0
    g = 0
    for i in range(0, len(rainy)):
        if rainy[i] == "yes":
            f = f + 1
        elif rainy[i] == "no":
            g = g + 1
    # print(f)
    # print(g)
    f1 = f / len(rainy)
    f2 = math.log(f1, 2)
    f3 = -f1 * f2
    g1 = g / len(rainy)
    g2 = math.log(g1, 2)
    g3 = - g1 * g2
    G = f3 + g3
    # print(G)
    h = 0
    j = 0
    for i in range(0, len(overcast)):
        if overcast[i] == "yes":
            h = h + 1
        elif overcast[i] == "no":
            j = j + 1
    # print(h)
    # print(j)
    if j == 0:
        K = 0
    # print(K)
    IO = len(sunny) / len(val) * S + len(overcast) / len(val) * K + len(rainy) / len(val) * G
    # print(IO)
    GainOutlook = E - IO
    print(GainOutlook)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def GainTemp():
    global val
    outlook1 = data["temp"].values
    # print(outlook1)
    hot = []
    mild = []
    cool = []
    for i in range(0, len(outlook1)):
        if outlook1[i] == "hot":
            hot.append(val[i])
        elif outlook1[i] == "mild":
            mild.append(val[i])
        elif outlook1[i] == "cool":
            cool.append(val[i])
    #print("hot",hot)
    #print("mild",mild)
    #print("cool",cool)
    c = 0
    d = 0
    for i in range(0, len(hot)):
        if hot[i] == "yes":
            c = c + 1
        elif hot[i] == "no":
            d = d + 1
    # print(c)
    # print(d)
    y = c / len(hot)
    y1 = math.log(y, 2)
    v = d / len(hot)
    y2 = math.log(v, 2)
    S1 = -y * y1
    S2 = -v * y2
    S = S1 + S2
    #print(S)
    f = 0
    g = 0
    for i in range(0, len(mild)):
        if mild[i] == "yes":
            f = f + 1
        elif mild[i] == "no":
            g = g + 1
    # print(f)
    # print(g)
    f1 = f / len(mild)
    f2 = math.log(f1, 2)
    f3 = -f1 * f2
    g1 = g / len(mild)
    g2 = math.log(g1, 2)
    g3 = - g1 * g2
    G = f3 + g3
    #print(G)
    h = 0
    j = 0
    for i in range(0, len(cool)):
        if cool[i] == "yes":
            h = h + 1
        elif cool[i] == "no":
            j = j + 1
    # print(h)
    # print(j)
    h1 = h/len(cool)
    h2 = math.log(h1,2)
    h3 = -h1*h2
    j1 = j/len(cool)
    j2 = math.log(j1,2)
    j3 = -j1*j2
    K = h3 + j3
    #print(K)
    IO = len(hot) / len(val) * S + len(mild) / len(val) * G + len(cool) / len(val) *K
    #print(IO)
    GainOutlook = E - IO
    print(GainOutlook)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def GainHumidity():
    global val
    global E
    outlook1 = data["humidity"].values
    high = []
    normal = []
    c = 0
    d = 0
    c1= 0
    d1 = 0
    for i in range(0,len(outlook1)):
        if outlook1[i] == "high":
            high.append(val[i])
        elif outlook1[i] == "normal":
            normal.append(val[i])
    for i in range(0,len(high)):
        if high[i] == "yes":
            c = c+1
        elif high[i] == "no":
            d = d+1
    for i in range(0,len(normal)):
        if normal[i] == "yes":
            c1 = c1+1
        elif normal[i] == "no":
            d1 = d1+1
    f1 = c / len(high)
    f2 = math.log(f1, 2)
    f3 = -f1 * f2
    g1 = d / len(high)
    g2 = math.log(g1, 2)
    g3 = - g1 * g2
    G = f3 + g3
    L1 = c1 / len(normal)
    L2 = math.log(L1, 2)
    L3 = -L1 * L2
    M1 = d1 / len(normal)
    M2 = math.log(M1, 2)
    M3 = - M1 * M2
    MMM = L3 + M3
    IO = len(high) / len(val) * G + len(normal) / len(val) * MMM
    GainOutlook = E - IO
    print(GainOutlook)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def GainWindy():
    global val
    global E
    outlook1 = data["windy"].values
    #print(outlook1)
    #print(len(outlook1))
    false = []
    true = []

    for i in range(0,len(outlook1)):
        if outlook1[i] == "Wind":
            true.append(val[i])
        elif outlook1[i] == "NoWind":
            false.append(val[i])
    #print(false)
    #print(true)
    c = 0
    d =0
    c1 = 0
    d1 = 0
    for i in range(0, len(false)):
        if false[i] == "yes":
            c = c + 1
        elif false[i] == "no":
            d = d + 1
    for i in range(0, len(true)):
        if true[i] == "yes":
            c1 = c1 + 1
        elif true[i] == "no":
            d1 = d1 + 1
    j1 = c/len(false)
    j2 = math.log(j1,2)
    j3 = -j1*j2
    j4 = d/len(false)
    j5 = math.log(j4,2)
    j6 = -j4*j5
    J = j3 + j6

    H1 = c1 / len(true)
    H2 = math.log(H1, 2)
    H3 = -H1 * H2
    H4 = d1 / len(true)
    H5 = math.log(H4, 2)
    H6 = -H4 * H5
    H = H3 + H6
    IO = len(false) / len(val) * J + len(true) / len(val) * H
    # print(IO)
    GainOutlook = E - IO
    print(GainOutlook)

GainOut()
GainHumidity()
GainWindy()
GainTemp()
