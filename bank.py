import mysql.connector

class Customer:
    def __init__(self,uid,name,phone,address,amount):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.address = address
        self.amount = amount


    def showcustomer(self):
        print("==",self.uid,"->",self.name,"==")
        print("Names is:",self.name)
        print("Phone is:", self.phone)
        print("Address is:", self.address)
        print("Amount is:", self.amount)
        print("==============================")

class DBHelper:

    def saveCustomerInDb(self,cRef1):
        sql = "insert into bank values({},'{}','{}',{},10,'{}')".format(cRef1.uid,cRef1.name,cRef1.phone,cRef1.address,cRef1.amount)
        con = mysql.connector.connect(user="root",password="",host="localhost",database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer saved !!")

    def updateCustomerInDb(self,redmPoints,phone):
        sql = "update bank set Amount = '{}' where phone ='{}'".format(redmPoints,phone)
        con = mysql.connector.connect(user="root",password="",host="localhost",database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer updated !!")


    def deleteCustomerInDb(self,name):
        sql = "delete from bank where phone = '{}'".format(phone)
        con = mysql.connector.connect(user="root",password="",host="localhost",database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer deleted !!")

    def fetchDetailsFromDB(self):
        sql = "select * from bank"
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            cRef = Customer(row[0],row[1],row[2],row[3],row[4])
            cRef.showcustomer()
            print()


def addCustomer():
    uid = int(input("Enter the User Id: "))
    name = input("Enter the name: ")
    phone = input("Enter the phone no.: ")
    amount = input("Enter the amount: ")

    cRef1 = bank(uid, name, phone,amount)
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
"""
phone = input("Enter the phone no.")
sql = "select * from bank where phone = '{}'".format(phone)
con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
cursor = con.cursor()
cursor.execute(sql)
row = cursor.fetchone()
"""

def redmptnAdd():
    price = int(input("Enter the amount you want to add:"))
    redmPoints = (price) + row[4]
    print("Update points are:", redmPoints)
    updateCustomer(redmPoints, phone)

def redmptnSub():
    price = int(input("Enter the amount you want to Withdraw:"))
    redmPoints =  row[4] - price
    print("Update points are:", redmPoints)
    updateCustomer(redmPoints, phone)


phone = input("Enter the phone no.")
sql = "select * from bank where phone = '{}'".format(phone)
con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
cursor = con.cursor()
cursor.execute(sql)
row = cursor.fetchone()


if row is not None:
    print("Yes! Phone no. exists")
    print("Balance Amount is:", row[4])

    #if price >= 10:
    reply = input("Do you want to Add Amount?")

    if reply == "yes":

     redmptnAdd()
    else:
        redmptnSub()

elif row is None :
    print("Phone no. does not exist!!")
    print("Add this customer as new one!!")
    addCustomer()
