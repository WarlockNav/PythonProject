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
