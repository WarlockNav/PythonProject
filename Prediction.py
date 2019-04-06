from tkinter import *
import mysql.connector
from sklearn.linear_model import LinearRegression


sql = "select Age from report"
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patient")
cursor = con.cursor()
cursor.execute(sql)
age = cursor.fetchall()
print(">>", age)


def onclick():
    print("!!")

    def fun2():
        print("!!")

        sql = "select Cholestrol from report"
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patient")
        cursor = con.cursor()
        cursor.execute(sql)
        chol = cursor.fetchall()
        # print(">>", rows)
        X = age
        Y = chol
        # X = X.reshape(len(X), 1)
        # Y = Y.reshape(len(Y), 1)
        regression = LinearRegression()

        regression.fit(X, Y)

        Y2 = regression.predict(X)
        # print(Y2)
        print(int(Y2[-1, 0]))
        lbl1 = Label(w1,text=Y2[-1, 0])
        lbl1.pack()

    def fun3():
        print("!!")
        sql = "select Blood_Pressure from report"
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patient")
        cursor = con.cursor()
        cursor.execute(sql)
        pressure = cursor.fetchall()
        # print(">>", rows)
        X = age
        Y = pressure
        # X = X.reshape(len(X), 1)
        # Y = Y.reshape(len(Y), 1)
        regression = LinearRegression()

        regression.fit(X, Y)

        Y2 = regression.predict(X)
        # print(Y2)
        print(int(Y2[-1, 0]))
        lbl1 = Label(w1, text=Y2[-1, 0])
        lbl1.pack()

    def fun4():
        print("!!")
        sql = "select Blood_Sugar from report"
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patient")
        cursor = con.cursor()
        cursor.execute(sql)
        sugar = cursor.fetchall()
        # print(">>", rows)
        X = age
        Y = sugar
        # X = X.reshape(len(X), 1)
        # Y = Y.reshape(len(Y), 1)
        regression = LinearRegression()

        regression.fit(X, Y)

        Y2 = regression.predict(X)
        # print(Y2)
        print(int(Y2[-1, 0]))
        lbl1 = Label(w1, text=Y2[-1, 0])
        lbl1.pack()

    def fun5():
        print("!!")
        sql = "select TSH from report"
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patient")
        cursor = con.cursor()
        cursor.execute(sql)
        tsh = cursor.fetchall()
        # print(">>", rows)
        X = age
        Y = tsh
        # X = X.reshape(len(X), 1)
        # Y = Y.reshape(len(Y), 1)
        regression = LinearRegression()

        regression.fit(X, Y)

        Y2 = regression.predict(X)
        # print(Y2)
        print(int(Y2[-1, 0]))
        lbl1 = Label(w1, text=Y2[-1, 0])
        lbl1.pack()

    def fun6():
        print("!!")
        sql = "select T3 from report"
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patient")
        cursor = con.cursor()
        cursor.execute(sql)
        ch = cursor.fetchall()
        # print(">>", rows)
        X = age
        Y = ch
        # X = X.reshape(len(X), 1)
        # Y = Y.reshape(len(Y), 1)
        regression = LinearRegression()

        regression.fit(X, Y)

        Y2 = regression.predict(X)
        # print(Y2)
        print(int(Y2[-1, 0]))
        lbl1 = Label(w1, text=Y2[-1, 0])
        lbl1.pack()

    def fun7():
        print("!!")
        sql = "select T4 from report"
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patient")
        cursor = con.cursor()
        cursor.execute(sql)
        tw = cursor.fetchall()
        # print(">>", rows)
        X = age
        Y = tw
        # X = X.reshape(len(X), 1)
        # Y = Y.reshape(len(Y), 1)
        regression = LinearRegression()

        regression.fit(X, Y)

        Y2 = regression.predict(X)
        # print(Y2)
        print(int(Y2[-1, 0]))
        lbl1 = Label(w1, text=Y2[-1, 0])
        lbl1.pack()

    w1 = Tk()
    button2 = Button(w1, text="Cholestrol Prediction", command=fun2)
    button2.pack()

    button3 = Button(w1, text="Blood Pressure Prediction", command=fun3)
    button3.pack()

    button4 = Button(w1, text="Blood Sugar Prediction", command=fun4)
    button4.pack()

    button5 = Button(w1, text="TSH Prediction", command=fun5)
    button5.pack()

    button6 = Button(w1, text="T3 Prediction", command=fun6)
    button6.pack()

    button7 = Button(w1, text="T4 Prediction", command=fun7)
    button7.pack()
    w1.mainloop()

def fun1():
    #print("!!")

    class Patient:

        def __init__(self, Cholestrol, Blood_Pressure, Blood_Sugar, Age, TSH, T3, T4):
            self.Cholestrol = Cholestrol
            self.Blood_Pressure = Blood_Pressure
            self.Blood_Sugar = Blood_Sugar
            self.Age = Age
            self.TSH = TSH
            self.T3 = T3
            self.T4 = T4

    class DBHelper:

        def saveCustomerInDB(self, cRef):
            sql = "insert into report values({}, {}, {}, {}, {}, {},{})".format(cRef.Cholestrol, cRef.Blood_Pressure,
                                                                                cRef.Blood_Sugar, cRef.Age,
                                                                                cRef.TSH, cRef.T3, cRef.T4)
            con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patient")
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            print(">> Customer Saved")

    Cholestrol = entrychol.get()
    Blood_Pressure = entryprs.get()
    Blood_Sugar = entrysuga.get()
    Age = entryage.get()
    TSH = entrytsh.get()
    T3 = entryt3.get()
    T4 = entryt4.get()
    #print(Cholestrol,Blood_Pressure,Blood_Sugar,Age,TSH,T3,T4)
    cRef = Patient(Cholestrol,Blood_Pressure,Blood_Sugar,Age,TSH,T3,T4)
    dbRef = DBHelper()
    dbRef.saveCustomerInDB(cRef)

window = Tk()
lbl1 = Label(window,text="Cholestrol")
lbl1.pack()
entrychol = Entry(window) # Rectangular TextField where user will enter data
entrychol.pack()
lbl2 = Label(window,text="Blood Pressure")
lbl2.pack()
entryprs = Entry(window) # Rectangular TextField where user will enter data
entryprs.pack()
lbl3 = Label(window,text="Blood Sugar")
lbl3.pack()
entrysuga = Entry(window) # Rectangular TextField where user will enter data
entrysuga.pack()
lbl4 = Label(window,text="Age")
lbl4.pack()
entryage = Entry(window) # Rectangular TextField where user will enter data
entryage.pack()
lbl5 = Label(window,text="TSH")
lbl5.pack()
entrytsh = Entry(window) # Rectangular TextField where user will enter data
entrytsh.pack()

lbl6 = Label(window,text="T3")
lbl6.pack()
entryt3 = Entry(window) # Rectangular TextField where user will enter data
entryt3.pack()

lbl7 = Label(window,text="T4")
lbl7.pack()
entryt4 = Entry(window) # Rectangular TextField where user will enter data
entryt4.pack()

button1 = Button(window,text = "Submit",command=fun1)
button1.pack()

button = Button(window,text = "Prediction",command=onclick)
button.pack()

window.mainloop()

