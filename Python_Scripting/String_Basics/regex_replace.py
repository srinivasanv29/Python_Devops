import re

text = "The quick brown fox jumps over the lazy pink chimpanzee"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)