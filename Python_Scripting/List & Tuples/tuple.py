## Tuple objects are below // You will get error
# Tuple object has no attribute append
print("tuple")
s3_buckets_list = ("user1_demo", "user2_bkp", "User3_archive")
s3_buckets_list.append("new_s3_bucket")
print(s3_buckets_list)

# Tuple is immutable ; once list is added we cannot amend. 