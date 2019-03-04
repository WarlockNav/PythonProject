import mysql.connector
import datetime as dt
class customer:
    def __init__(self,uid,name,phone,Address,Amount):
        self.uid = uid
        self.name = name
        self.phone = phone
        self.Address = Address
        self.Amount = Amount
    def show(self):
        print("Uid",self.uid)
        print("Name", self.name)
        print("Phone", self.phone)
        print("Address", self.Address)
        print("Amount", self.Amount)
class DBHelper:
    def saveCustomerInDb(self, cRef1):
        sql = "insert into bank values({},'{}','{}','{}',{})".format(cRef1.uid, cRef1.name, cRef1.phone,
                                                                        cRef1.Address, cRef1.Amount)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer saved !!")

    def updateCustomerInDb(self, redmPoints,phone):
        sql = "UPDATE bank SET Amount = {}  where phone ='{}'".format(redmPoints,phone)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer updated !!")

    def deleteCustomerInDb(self, name):
        sql = "delete from bank where phone = '{}'".format(phone)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        #print(">> Customer deleted !!")

    def updateTransaction(self,value,phone):
        sql = "UPDATE bank SET transaction ='{}' WHERE phone = '{}' ".format(value,phone)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Transaction time is:",value)

    def fetchDetailsFromDB(self):
        sql = "select * from bank"
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            cRef = Customer(row[0], row[1], row[2], row[3], row[4])
            cRef.showcustomer()
            print()


def addCustomer():
    uid = int(input("Enter the User Id: "))
    name = input("Enter the name: ")
    phone = input("Enter the phone no.: ")
    Address = input("Enter the amount: ")
    Amount = input("Enter the amount: ")

    cRef1 = customer(uid, name, phone,Address,Amount)
    cRef1.show()
    dbhelper = DBHelper()
    dbhelper.saveCustomerInDb(cRef1)


def updateCustomer(redmPoints,phone):
    dbhelper = DBHelper()
    value = dt.datetime.now()
    dbhelper.updateCustomerInDb(redmPoints,phone)
    dbhelper.updateTransaction(value, phone)

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
    updateCustomer(redmPoints,phone)
def redmptnSub1(price):
    #price = int(input("Enter the amount you want to Transfer:"))
    redmPoints =  row[4] - price
    print("Your balance Amount is:", redmPoints)
    today = dt.datetime.today()
    updateCustomer(redmPoints,phone)
def redmptnAdd1(price):
    phone = input("Enter the phone no. to whom You transfer the money->")
    sql = "select * from bank where phone = '{}'".format(phone)
    con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
    cursor = con.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()

    if row is not None:
        print("Their Balance Amount is:", row[4])
        redmPoints = row[4] + price
        print("Their updated Balance is:",redmPoints)
        today = dt.datetime.today()
        updateCustomer(redmPoints,phone)
    elif row is None:
        print("Phone no. does not exist!!")
        print("Add this customer as new one!!")
        addCustomer()


def transfer():
    b = input("Do you want to transfer the money?")
    if b == "yes":
        price = int(input("How much money you want to transfer??"))
        redmptnAdd1(price)
        redmptnSub1(price)
    else:
        print("//")
def redmptnSub():
    a = input("Do you want to withdraw money?")
    if a == "yes":
        price = int(input("Enter the amount you want to Withdraw:"))
        redmPoints = row[4] - price
        print("Update points are:", redmPoints)
        today = dt.datetime.today()

        updateCustomer(redmPoints,phone)
    else:
        transfer()


phone = input("Enter the phone no.")
sql = "select * from bank where phone = '{}'".format(phone)
con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
cursor = con.cursor()
cursor.execute(sql)
row = cursor.fetchone()

if row is not None:
    print("Yes! Phone no. exists")
    print("Balance Amount is:", row[4])
    print("Last Transaction is at:", row[6])
    # if price >= 10:
    reply = input("Do you want to Add Amount?")

    if reply == "yes":

        redmptnAdd()
    elif reply == "no":
         redmptnSub()
    else:
        print("//")

elif row is None:
    print("Phone no. does not exist!!")
    print("Add this customer as new one!!")
    addCustomer()
