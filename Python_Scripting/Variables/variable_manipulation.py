# Define configuration variable 
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# Print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max connections allowed: {max_connections}")

# Update configuration values
port = 443
is_https_enabled = False

print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enabled}")

# This allows us to easily manage and update Devops cofig files.
