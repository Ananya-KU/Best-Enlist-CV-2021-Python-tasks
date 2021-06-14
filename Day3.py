#importing library
from tkinter import *
import tkinter.messagebox
#Declaring root
root =Tk()
root.title("Employee Registration Form")
root.geometry('800x600')
root.configure(background = "lightpink")

label1=Label(root ,text= "Employee Registration Form ", font=("bold", 20)).grid(row =0, column=2)

Firstname = Label(root ,text = "First Name",width=20,font=("bold", 10)).grid(row = 1,column = 1)
LastName = Label(root ,text = "Last Name",width=20,font=("bold", 10)).grid(row = 2,column = 1)
Empid=Label(root,text="Employee ID",width=20,font=("bold", 10)).grid(row = 3,column = 1)
Address = Label(root,text = "Address",width=20,font=("bold", 10)).grid(row = 4,column = 1)
City = Label(root ,text = "City",width=20,font=("bold", 10)).grid(row = 5,column = 1)
State= Label(root,text = "state",width=20,font=("bold", 10)).grid(row = 6,column = 1)
Country = Label(root ,text = "Country",width=20,font=("bold", 10)).grid(row = 7,column = 1)
list1 = ['US','Canada','India','UK','Nepal','Iceland','South Africa']

c=StringVar()

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.grid(row = 7,column = 2)
Mobile = Label(root ,text = "Contact Number",width=20,font=("bold", 10)).grid(row = 8,column = 1)
Email = Label(root ,text = "Email Id",width=20,font=("bold", 10)).grid(row = 9,column = 1)
Gender =Label(root ,text = "Gender",width=20,font=("bold", 10)).grid(row = 10,column = 1)

var = IntVar()

Radiobutton(root, text="Male",padx = 30, variable=var, value=1).grid(row = 10,column = 2)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).grid(row = 10,column = 3)
Choose =Label(root ,text = "Date Of Birth",width=20,font=("bold", 10)).grid(row = 11,column = 1)
label_12 = Label(root, text="Programming",width=20,font=("bold", 10))
label_12.grid(row = 12,column = 1)

var1 = IntVar();
Checkbutton(root, text="java", variable=var1).grid(row = 12,column = 2)

var2 = IntVar();
Checkbutton(root, text="python", variable=var2).grid(row = 12,column = 3)

# Creating CheckBox
# The variable 'variable' mentioned here holds Integer value, by default 0
variable=IntVar()

# This will creates checkbutton widget and uses place() method.
Checkbutton(root,text="I Accept all Term and Conditions", variable=variable).place(x=80,y=350)

Firstname1 = Entry(root).grid(row = 1,column = 2)
Lastname1 = Entry(root).grid(row = 2,column = 2)
Empid1=Entry(root).grid(row=3,column=2)
Adderss1=Entry(root).grid(row = 4,column = 2)
city1=Entry(root).grid(row = 5,column = 2)
state1=Entry(root).grid(row = 6,column = 2)
Email1 = Entry(root).grid(row = 9,column = 2)
Mobile1 = Entry(root).grid(row = 8,column = 2)
choose1 = Entry(root).grid(row = 11,column = 2)


def onClick():
    tkinter.messagebox.showinfo("Welcome", "Your Details Submitted  Successfully !")

# Create a Button
Button(root, text="Submit", command=onClick,width=25,bg='red',fg='white').grid(row = 14,column = 2)

root.mainloop()

