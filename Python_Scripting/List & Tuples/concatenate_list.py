s3_buckets_list = ("user1_demo", "user2_bkp", "User3_archive", "new_s3_bucket")
print(s3_buckets_list[0] + s3_buckets_list[1])

# Result will be like below. 
##  user1_demouser2_bkp

s3_buckets_list = ("user1_demo", "user2_bkp", "User3_archive", "new_s3_bucket")
print(s3_buckets_list[0] + "---" + s3_buckets_list[1])

# user1_demo---user2_bkp
