class Order:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def showOrder(self):
        print("====",self.name,"====")
        print("Price:\u20b9",self.price)
        print("Quantity:", self.quantity)
        if self.quantity >= 3:
            a = ["XXAA15","EETT40","BOGO"]
            code = input("Enter the Promo Code: ")
            if code == a[0]:
                print(self.price*50//100,"50% discount on your Order")
            elif code == a[1]:
                print(self.price *60// 100, "60% discount on your Order")
            elif code == a[2]:
                print(self.price *70// 100, "70% discount on your Order")
            else:
                print("Invalid Code")
        else:
            print("discount is avialable on minimum 3 dishes")

#s1 = Order("Pizza",500,3)
s2 = Order("Burger",500,2)
s2.showOrder()
