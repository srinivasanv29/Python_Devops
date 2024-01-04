# Get pull request information on a repo; using python 

# On your machine you need to write python script to interact with Github. 
# either you can use API to interact with GitHub or you can use CLI

# When you are writing script by yourself you use API model. First you need to identify the 
# module that is used to talk to GitHub API.

Module --> request
# 1. using this request module need to make API call. 
# 2. You also need to know what is the URL to make the API call
# 3.  Tool interacting with provide JSON format output.
# Once we received json information we need to convert this to Dictionary, because python cannot perform directly on the JSON, it can only perform on native data types, closest one is Dictionary.
# 
# 4. print the requirement

What is the URL for the pull request. 

Google > search for > Github API docs >> search in REST API references 
>> LOOKUP for pulls >> There you will get the repo url 

/repos/{owner}/{repo}/pulls

Start writing the code now. 

$ pip install requests 
$ 