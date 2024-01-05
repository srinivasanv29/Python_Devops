# To update a filed in application file automatically using python. This is important
# . What is file operation - when you want to read a file or update a file
# or read a file we need file operations 

# We can achieve same using shell scripting, python will help even if it is in
# different operating systems

# Two file opearation - read operation ; write operation

# e.g read what is in line no 5 ; If you want to add or amend a new license

# Here in python we will use "inbuilt functions".

# To open a file in python use with as a statement 

Syntax

with open ("/opt/test/usecases/utilities", "r") ## This is for read operation
with open ("/opt/test/usecases/utilities/test.abc", "w") ## This is for write operation

Scenario:
When maximum connection reaching 200 update server.conf File 

