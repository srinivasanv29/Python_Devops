# if you want to store list of dictionaries you have to use list datatype. 

# Dictionary

student_info = [
    {
        "name": "srini"
        "age": "10"
        "id": "1011"
        "class": "10"
    }
]


# Below is the example for list of dictionaries
student_info = [
    {},
    {},
    {},
]

# Below is the example for list of strings

name_list = [ "abi", "ram", "xavier"]

# Only difference is representation bw list of strings and list of dictionaries.

# ec2 instance info
# When there are multiple properties with complex structures we will use dictionaries. 

ec2_instance_info = [
    {
        "id": "instance-001",
        "type": "t2-micro"
    },
    {
        "id": "instance-002",
        "type": "t2-medium"
    },
    {
        "id": "instance-003",
        "type": "t2-xlarge"
    }
]

# inside list element 0, element 1, element 2 or index 0, index 1, index 2. 
print(ec2_instance_info[1]["type"])


