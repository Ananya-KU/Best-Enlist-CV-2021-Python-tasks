#Try And Catch
#List down all the error types and check all the errors using a python program for all errors
#list=12
print(list1)Name error

#Type error
a='123'
a+=123  # int is added with string
l=[1,2,3,4,5,56,6,7]
for i in range(2,l):
    print(i+1)

#Syntax error
for i range(1,10):  #for i in range(1,10):   in keyword missing
    print(i)
in =123 # keyword is used as variable

# index error
l=[1,2,3,4,5,56,6,7]
for i in range(len(l)):
    print(l[i+1])

#Module not found error
import modulexyz

#Key error
dict1=dict()
dict1={1:12,11:12,13:14}
print(dict1[23])

#Import error
from math import x

#Value error
int("abc")

#Zero Division Error
100/0

#Design a simple calculator app with try and except for all use cases
def calculate():
    try:
        print('+')
        print('-')
        print('*')
        print('/')
        print('%')
        print('**')
        operation = input("Select an operator:n")
        print("Enter two numbers")
        number_1 = int(input())
        number_2 = int(input())
        if operation == '+': # To add two numbers
            print(number_1 + number_2)
        elif operation == '-': # To subtract two numbers
            print(number_1 - number_2)
        elif operation == '*': # To multiply two numbers
            print(number_1 * number_2)
        elif operation == '/': # To divide two numbers
            print(number_1 / number_2)
        elif operation == '%': # To remainder two numbers
            print(number_1 % number_2)
        elif operation == '**': # To num1 exponent num2
            print(number_1 ** number_2)
        else:
            print('Invalid Input')
    except Exception as e:
        print(e)

calculate()

#print one message if the try block raises a NameError and another for other errors
try:
    a = 123
    if a==123:
        print(b)
        raise NameError("Name error")
    if a >0:
        raise ValueError("Value error")
except NameError as ne:
        print(ne)
except ValueError as ve:
    print(ve)

#Try getting an input inside the try catch block
try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')