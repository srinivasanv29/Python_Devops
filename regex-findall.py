import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("patten found:", search.group())
else:
    print("pattern not found")
