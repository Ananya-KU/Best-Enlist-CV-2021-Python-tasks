# Create a function getting two integer inputs from user and print the following
# Addition of two numbers is +value
# Subtraction of two numbers +value
# Multiplication of two numbers +value
def addition(x,y):
    print("addition of two numbers",(x+y))
def subtraction(x,y):
    print("subtraction of two numbers",(x-y))

def multiplication(x,y):
    print("multiplication of two numbers",(x*y))
def division(x,y):
    print("division of two numbers",(x/y))

x= int(input("enter the value of x"))
y= int(input("\nenter the value of y\n"))
addition(x,y)
subtraction(x,y)
division(x,y)
multiplication(x,y)

# Create a function covid() and its should accept patient name, and body temperature, by default the body temperature should be 98 degree.
def covid(patient_name, body_temp=98):
    patient_details = {'patient_name: name,''body_temp': body_temperature}
    print(patient_details)

patient_name = input('enter the patient name\n')
body_temperature = int(input('enter the patient body temperature'))
covid(patient_name, body_temperature)