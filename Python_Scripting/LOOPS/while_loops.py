# while loops


# SCENARIO 

# Incase you have to delete all the files in filesystem OR folder to be deleted then you will have to go with this WHILE LOOP 

while kubectl get deployment/myapp | grep -q 0/1; do
    echo "Waiting for myapp to be ready..."
    sleep 10
done