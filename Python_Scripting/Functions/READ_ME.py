# using function you have below features
# modularity (reusability)
# readability 
# Debugging

# function take inputs and return outputs

# primary responsibility - Take input >> perform logic >> return the output

def addition(num1, num2):
    add = num1 + num2
    return add  ## return keyword is used to replace the output in print(addition(5, 10))

def sub(num1, num2):
    sub = num1 - num2
    return sub

def mul(num1, num2):
    mul = num1 * num2
    return mul

print(addition(5, 10))
print(sub(10, 5))
print(mul(10, 5))

# This is the better way to write the programms by taking the input and return the output. 

# Packages is nothing but collection of modules; in your project writing 5 python files basically the application, 
# bundle all of these files into a package ; it is written 1000 of python files. some call it as package or library
# pacakages + modules we will use more

# writing an api for aws, jira, github api.. making any http request.. python package index (PYPI)
# https://pypi.org/search/?q=boto3  // You can use this link to search the package to install for AWS, Jira or any api or software associated to python.

