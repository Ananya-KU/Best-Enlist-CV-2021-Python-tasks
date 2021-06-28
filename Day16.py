# Create a lambda function that multiplies argument x with argument y
s = lambda x, y: x * y
print(s(12, 4))

# Write a Python program to create Fibonacci series to n using Lambda
from functools import reduce

fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                              range(n - 2), [0, 1])

print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))

# Write a Python program that multiply each number of given list with a given number
a_list = [1, 2, 3]

multiplied_list = [element * 2 for element in a_list]

print(multiplied_list)

# Write a Python program to find numbers divisible by 9 from a list of numbers
# Take a list of numbers
my_list = [18,22,27,30,36,45,81,118]
# use anonymous function to filter
result = list(filter(lambda x: (x % 9 == 0), my_list))
# display the result
print("Numbers divisible by 9 are",result)

# Write a Python program to count the even numbers in a given list of integers
# list of numbers
list1 = [10, 24, 4, 8, 45, 66, 93, 1, 9]
even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

