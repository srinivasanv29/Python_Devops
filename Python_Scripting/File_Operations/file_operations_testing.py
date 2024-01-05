# This program will iterate the file and amend the value inside the file

def update_server_config(file_path, key, value):
    
    with open(file_path, "r") as file:      ## This will read the file and save it in variable called lines
        lines = file.readlines()

    with open(file_path, "w") as file:      ## This will write the file , lines o/p given as input to line.. from there using the key the value will be changed //
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n") 
            else: 
                file.write(line)


update_server_config("/tmp/server_sysctl.conf", "MAX_CONNECTIONS", "500500")  ## Here we are giving the value declared in function.
