import mysql.connector

class Customer:
    def __init__(self,cid,name,phone,age,address):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.age = age
        self.address = address

    def showcustomer(self):
        print("==",self.cid,"->",self.name,"==")
        print("Names is:",self.name)
        print("Phone is:", self.phone)
        print("Age is:", self.age)
        print("Address is:", self.address)
        print("==============================")

class DBHelper:

    def saveCustomerInDb(self,cRef1):
        sql = "insert into customer1 values({},'{}','{}',{},10,'{}')".format(cRef1.cid,cRef1.name,cRef1.phone,cRef1.age,cRef1.address)
        con = mysql.connector.connect(user="root",password="",host="localhost",database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer saved !!")

    def updateCustomerInDb(self,redmPoints,phone):
        sql = "update customer1 set points = '{}' where phone ='{}'".format(redmPoints,phone)
        con = mysql.connector.connect(user="root",password="",host="localhost",database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer updated !!")


    def deleteCustomerInDb(self,name):
        sql = "delete from customer1 where phone = '{}'".format(phone)
        con = mysql.connector.connect(user="root",password="",host="localhost",database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer deleted !!")

    def fetchDetailsFromDB(self):
        sql = "select * from customer1"
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            cRef = Customer(row[0],row[1],row[2],row[3],row[4])
            cRef.showcustomer()
            print()

def addCustomer():
    name = input("Enter the name:")
    phone = input("Enter the phone no.:")
    age = input("Enter the age:")
    address = input("Enter the address:")

    cRef1 = Customer(12, name, phone, age, address)
    cRef1.showcustomer()
    dbhelper = DBHelper()
    dbhelper.saveCustomerInDb(cRef1)


def updateCustomer(lpoints,phone):
    dbhelper = DBHelper()
    dbhelper.updateCustomerInDb(lpoints,phone)


def delCustomer():
    phone = input("Enter the mobile no. you want to delete:")
    dbhelper = DBHelper()
    dbhelper.deleteCustomerInDb(phone)

def seeCustomer():
    dbhelper = DBHelper()
    dbhelper.fetchDetailsFromDB()

phone = input("Enter the phone no.")
sql = "select * from customer1 where phone = '{}'".format(phone)
con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
cursor = con.cursor()
cursor.execute(sql)
row = cursor.fetchone()


def redmptnAdd():
    redmPoints = (price * 10 // 100) + row[4]
    print("Update points are:", redmPoints)
    updateCustomer(redmPoints, phone)

def redmptnSub():
    redmPoints = ((price * 10 // 100) + row[4]) - reply2
    print("Update points are:", redmPoints)
    updateCustomer(redmPoints, phone)

if row is not None:
    print("Yes! Phone no. exists")
    print("Previous points are:", row[4])
    price = int(input("Enter the price:"))

    if price >= 500:
        reply = input("Do you want to redeem points?")

        if reply == "no":
            redmptnAdd()

        elif reply == "yes":
            reply2 = int(input("How namy points you want to redeem?"))
            redmptnSub()
    else:
        redmptnAdd()

elif row is None :
    print("Phone no. does not exist!!")
    print("Add this customer as new one!!")
    addCustomer()
