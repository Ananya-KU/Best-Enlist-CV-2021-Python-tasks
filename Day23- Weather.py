# 2.Create another button as ‘fetch button’ and have a functionality of fetching the weather on a given location in text box
import json
import requests
from tkinter import *
from PIL import ImageTk,Image

# Required Details
root = Tk()
root.geometry("650x450")
root.title("Weather App")
root.configure(bg='white')

# for images

img = ImageTk.PhotoImage(Image.open('images.jpg'))
panel = Label(root,image=img)
panel.place(x=270,y=15)

lable_0 = Label(root,text="Current Weather",width=15,bg='white',font=("bold",20),fg='red')
lable_0.place(x=0,y=40)

city_names = StringVar()
entry_1 = Entry(root,textvariable=city_names)
city_names.set("Enter City Here ...")
entry_1.place(x=90,y=130)



lable_2 = Label(root,text="Temprature : ",width = 20,bg='white',font=("bold",10),fg='blue')
lable_2.place(x=62,y=220)

lable_3 = Label(root,text="Pressure : ",width = 20,bg='white',font=("bold",10),fg='blue')
lable_3.place(x=62,y=240)

lable_5 = Label(root,text="Description : ",width = 20,bg='white',font=("bold",10),fg='blue')
lable_5.place(x=62,y=260)

lable_temp = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_temp.place(x=192,y=220)

lable_pres = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_pres.place(x=192,y=240)

lable_desc = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_desc.place(x=192,y=260)



# api config
def getTemp():

    api_key = "07bc42b43f27cebcc612fb3cde5dea00"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = entry_1.get()
    complete_url = base_url+"appid="+api_key+"&q="+city_name

# module response get

    response = requests.get(complete_url)
    x=response.json()

    if["cod"] !='404':
        y = x["main"]
        current_temprature = y["temp"]
        current_pressure = y["pressure"]

        z = x["weather"]
        weather_description = z[0]["description"]

        lable_pres.configure(text=current_pressure)
        lable_temp.configure(text=current_temprature)
        lable_desc.configure(text=weather_description)
    else:
        lable_pres.configure(text="Err")
        lable_temp.configure(text="Err")
        lable_desc.configure(text="Err")

Button(root,text="Submit",width=10,bg='brown',fg='white',command=getTemp).place(x=125,y=180)

lable_unit = Label(root,text="Temprature in Kelvin And Pressure in mb",width = 35,bg='white',font=("bold",12),fg='brown')
lable_unit.place(x=30,y=300)

lable_unit = Label(root,text="-By ANANYA K.U",width = 35,bg='white',font=("bold",10),fg='brown')
lable_unit.place(x=35,y=350)

mainloop()

