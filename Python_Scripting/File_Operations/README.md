# Only for learning:

# Change a value in linux or unix server config file

Tasks:

a) open the file ; read the File
b) store everything in a variable called -> list
c) open the file ; write a File (updateing a maximum connections)

def update_server_config(filepath, key, value):
    
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else: 
                file.write(line)


update_server_config("/tmp/server_sysctl.conf", "maximum_connections", "500")