s3_buckets_list = ["user1_demo", "user2_bkp", "User3_archive", "new_s3_bucket"]
print(len(s3_buckets_list))

s3_buckets_list.append("Anto_demo_bucket")
print(len(s3_buckets_list))

s3_buckets_list.remove("User3_archive")
s3_buckets_list.remove("user2_bkp")
print(len(s3_buckets_list))
