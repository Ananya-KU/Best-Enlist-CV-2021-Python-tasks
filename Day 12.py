# Create a file 30 days 30 hour operations
# Write data in it I have completed 10 days successfully.
# Append the data your name in to it.
# Close the file.
f =open(r"30_days_30_hour_operations.txt","w+")
f.write("I have completed 12 days successfully\t")
f.close()

f1 =open(r"30_days_30_hour_operations.txt","a+")
f1.writelines("Amogha M")


f1 =open(r"30_days_30_hour_operations.txt","r")
print(f1.read())

f1.close()