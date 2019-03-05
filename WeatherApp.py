from tkinter import *
import json
import requests

def onClick1():
    CityName = entryT1.get()
    url = "https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(CityName)
    response = requests.get(url)
    print(response.text)
    data = json.loads(response.text)
    lol = data["main"]["temp"]
    lw = data["main"]["pressure"]
    lc = data["main"]["humidity"]
    lbl1.config(text='Temperature:' + str(lol))
    lbl2.config(text='pressure:' + str(lw))
    lbl3.config(text='Humidity:' + str(lc))
"""
def onClick2():
    global response
    setT2.set(response)
"""
window = Tk()

lblTitle = Label(window, text="Weather App :")
lblTitle.pack()

lblT1= Label(window, text="Enter the City Name:")
lblT1.pack()

entryT1 = Entry(window)
entryT1.pack()

btnAddMoney = Button(window, text="Show", command=onClick1)
btnAddMoney.pack()

#lblT2 = Label(window, text="Temperature :",command=onClick2)
#lblT2.pack()
#setT2 = set(window)
#setT2.pack()
lbl1 = Label(window)
lbl1.pack()
lbl2 = Label(window)
lbl2.pack()
lbl3 = Label(window)
lbl3.pack()
window.mainloop()
