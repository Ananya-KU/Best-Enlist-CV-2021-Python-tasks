# Write a python script to merge two python dictionaries
# Python code to merge dict using a single expression
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

# Write a python program to remove a key from a dictionary
# Dictionary of strings and int
word_freq_dict = {"Hello": 56, "at": 23, "test": 43,"this": 43}
key_to_be_deleted = 'at'
new_dict = {}
for key, value in word_freq_dict.items():
    if key is not key_to_be_deleted:
        new_dict[key] = value
word_freq_dict = new_dict

print(word_freq_dict)

# Write a python program to map two lists into a dictionary
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

# Write a python program to find the length of a set
#Create a set
setn = {5, 10, 3, 15, 2, 20}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nLength of the set:")
print(len(setn))

# Write a python program to remove the intersection of a 2nd set from the 1st set
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("\nRemove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print("sn1: ",sn1)
print("sn2: ",sn2)
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("\nRemove the intersection of a 2nd set from the 1st set using -= operator:")
sn1-=sn2
print("sn1: ",sn1)
print("sn2: ",sn2)
