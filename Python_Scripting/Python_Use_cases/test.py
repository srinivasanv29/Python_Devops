import os

folders = input("please provide list of folder names with spaces in between: " ).split()


for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide valid folder name, looks like given folder does not exist" + folder)
        break  ## To terminate the execution of the for loops we will use break statement
    except PermissionError:
        break
        print("No access to folder:" + folder)

        print(" ==== listing files for the respective dir -" + folder)

    for file in files:
        print(file)
# We need os module ; os module talks to operating system.
        
# If user giving input to division 5 / 0 - no number can be divided by zero, so you "zerodivison error" have to be used
# as an exception. 