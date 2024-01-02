# To import env variables from CLI -- import the variables from CLI 
# e.g from linux shell [ "$ export password="abc$123"  ] and then you can 
# write script like below to 

# "$ export apitoken="346rt73fvedveoioi£@$£@gi8"
# If you are running the job in CICD, jenkins etc only script will be available to run or execute. We are keeping information protected.
# or secured in this way.

import os
print(os.getenv("password"))
print(os.getenv("apitoken"))