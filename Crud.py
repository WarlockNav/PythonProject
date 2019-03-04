import mysql.connector

# Model : which will hold data
class Customer:

    def __init__(self, cid, name, phone, age, address,points):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.age = age
        self.address = address
        self.points = points


    def showCustomer(self):
        print("==", self.cid, "|", self.name, "==")
        print("Name", self.name)
        print("Phone", self.phone)
        print("Age", self.age)
        print("Points", self.points)
        print("Address", self.address)
        print("==============")

# DAO or Data Access Object : Used to perform DB Operations
# CRUD Operations -> Create Retrieve Update and Delete
class DBHelper:

    def saveCustomerInDB(self, cRef):
        sql = "insert into customer1 values('{}', '{}', '{}', {}, 10, '{}')".format(cRef.cid,cRef.name, cRef.phone, cRef.age,cRef.address,
                                                                               cRef.points,)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer Saved")

    def updateCustomerInDB(self, cRef):
        sql = "update customer1 set name = '{}', phone='{}', age={}, address = '{}' where cid = {}".format(cRef.name, cRef.phone, cRef.age,
                                                          cRef.address, cRef.cid)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer Updated")

    def deleteCustomerFromDB(self, cid):
        sql = "delete from customer1 where cid = {}".format(cid)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">> Customer Deleted")

    def fetchCustomersFromDB(self):
        sql = "select * from customer1"
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)

        """
        row = cursor.fetchone()
        print(">>",row)
        row = cursor.fetchone()
        print(">>", row)
        row = cursor.fetchone()
        print(">>", row)
        """

        rows = cursor.fetchall()
        # print(rows)
        # print(type(rows))
        for row in rows:
            # print(row)
            cRef = Customer(row[0], row[1], row[2], row[3], row[4])
            cRef.showCustomer()
            print()

pp = 100
cRef1 = Customer(10, "Hena", "+91 999944 769876", 25,"USA",pp)
cRef1.showCustomer()
dbRef = DBHelper()
dbRef.saveCustomerInDB(cRef1)


