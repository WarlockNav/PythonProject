# To Create GUI we have tkinter
from tkinter import *
from assignment import *

# onClick can be any name of your choice
def onClick():
    print("Button Clicked")
    cid = entrycid.get()
    name = entryName.get()
    phone = entryPhone.get()

    age = entryAge.get()
    #points = entrypoints.get()
    address = entryAddress.get()

    print(cid,"|",name,"|",phone,"|",age,"|",address)

    # Create Customer Object
    cRef = Customer(cid,name,phone,int(age),address)

    # Create DBHelper Object
    dbHelper = DBHelper()
    dbHelper.saveCustomerInDb(cRef)


window = Tk()

lblTitle = Label(window, text="Add Customer Details Below:")
lblTitle.pack() # Pack the Label in Window

lblcid = Label(window, text="Enter Customer Id:")
lblcid.pack() # Pack the Label in Window

entrycid = Entry(window) # Rectangular TextField where user will enter data
entrycid.pack()

lblName = Label(window, text="Enter Customer Name:")
lblName.pack() # Pack the Label in Window

entryName = Entry(window) # Rectangular TextField where user will enter data
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone:")
lblPhone.pack() # Pack the Label in Window

entryPhone = Entry(window) # Rectangular TextField where user will enter data
entryPhone.pack()

lblAge = Label(window, text="Enter Customer Age:")
lblAge.pack() # Pack the Label in Window

entryAge = Entry(window) # Rectangular TextField where user will enter data
entryAge.pack()

#lblpoints = Label(window, text="Enter Customer Points:")
#lblpoints.pack() # Pack the Label in Window
#entrypoints = Entry(window) # Rectangular TextField where user will enter data
#entrypoints.pack()


lblAddress = Label(window, text="Enter Customer Address:")
lblAddress.pack() # Pack the Label in Window

entryAddress = Entry(window) # Rectangular TextField where user will enter data
entryAddress.pack()

btnAddCustomer = Button(window, text="Add Customer", command=onClick)
btnAddCustomer.pack()

# Keep on running the process
window.mainloop()
