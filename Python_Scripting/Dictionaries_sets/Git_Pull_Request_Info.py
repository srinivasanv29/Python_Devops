# This program used to integrate github with Python
# Git pull request information of a repo
import requests

# "api.github.com/repos/kubernetes/kubernetes/pulls" 

#  copy paste this in browser you can see the details manually, we are going to 
# pull the data as it shown in browser using requests.get in PYTHON. 

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
print(type(response))




