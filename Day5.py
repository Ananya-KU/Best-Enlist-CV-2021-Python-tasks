# Write a program to create a list of n integer values and do the following
# Add an item in to the list(using function)
# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)
List.append(5)
print("\nList after Addition of Three elements: ")
print(List)
# Delete(using function)
del List[0]
print(List)
# Store the largest number from the list to a variable
list1 = [3, 2, 8, 5, 10, 6]
max_number = max(list1);
print("The largest number is:", max_number)
# Store the smallest number from the list to a variable
list1 = [3, 2, 8, 5, 10, 6]
min_number = min(list1);
print("The largest number is:", max_number)
# Addition of elements in a List
lst = [2,4,6,8,10,12,14]
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


# Create a tuple and print the reverse of the created tuple
tuples=(1,2,3,4,5,67,8)  #assuming set of tuples
reversedTuples = tuples[::-1] #slicing
print(reversedTuples)

#using in-built reversed() function
tuples=(1,2,3,4,5,67,8)
reversedTuples=tuple(reversed(tuples))
print(reversedTuples)


# Create a tuple and convert tuple into list
# Using list comprehension

# initializing tuple
test_tup = (5, 6, 7, 4, 9)
# printing original tuple
print("The original tuple is : ", test_tup)
# initializing K
K = "Gsd"
# list comprehension for nested loop for flatten
res = [ele for sub in test_tup for ele in (sub, K)]
# printing result
print("Converted Tuple with K : ", res)

